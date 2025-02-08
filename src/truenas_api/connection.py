import asyncio
import json
import logging
import uuid
from dataclasses import dataclass
from typing import Any, Dict, Optional

import websockets

# create logger for this module
logger = logging.getLogger(__name__)


@dataclass
class TrueNASResponse:
    id: str
    result: Any
    error: Optional[Dict]


class TrueNASConnection:
    def __init__(self, host: str, uname: str, passwd: str):
        """Initialize TrueNAS connection.

        Args:
            host: TrueNAS hostname/IP (e.g. 'truenas.local')
            uname: WebSocket API username
            passwd: WebSocket API password
        """
        self.host = host
        self.username = uname
        self._password = passwd
        self.websocket = None
        self.session_id = None
        self._msg_id_counter = 0  # For tracking API calls

        # log intitalization, but mask API key and/or password
        # since we're still working on the DDP websocket AP{I, ignore the
        # API key case for now
        masked_passwd = "***"
        logger.debug(
            "Initiazing TrueNAS connection to %s, username %s, password %s",
            self.host,
            self.username,
            masked_passwd,
        )

    def _generate_msg_id(self) -> str:
        """Generate a unique msg id for this message.

        Increments _msg_id_counter

        Returns: UUID
        """
        self._msg_id_counter += 1
        return str(uuid.uuid5(self.session_id, str(self._msg_id_counter)))

    def _mask_sensitive_params(self, params: list) -> list:
        """Mask sensitive dfata prior to logging

        Currently masks
        - API keys
        - Passwords
        - Authentication tokens
        """
        masked_params = []
        for param in params:
            if isinstance(param, str):
                if any(
                    term in str(param) for term in ["key", "pass", "token", "secret"]
                ):
                    masked_params.append("***")
                else:
                    masked_params.append(param)
            else:
                masked_params.append(param)
        return masked_params

    async def connect(self) -> None:
        """Establish WebSocket connection to TrueNAS.

        The connection process happens in two steps:
        1. Initial WebSocket connect with version handshake. Returns a session id.
        2. Authentication using the provided id, plus a username and password.

        Raises:
            ConnectionError: If connection cannot be established
            AuthenticationError: If auth creds are invalid
        """
        uri = f"ws://{self.host}/websocket"

        logger.info("Attempting to connect to TrueNAS at %s", uri)
        try:
            # open the websocket
            self.websocket = await websockets.connect(uri)
            logger.debug("WebSocket connection opened")
            # establish connection
            conn_msg = {"msg": "connect", "version": "1", "support": ["1"]}
            conn_msg_json = json.dumps(conn_msg)
            logger.debug("Sending connection request: %s", conn_msg_json)
            await self.websocket.send(conn_msg_json)
            res_json = await self.websocket.recv()
            res = json.loads(res_json)
            logger.debug("Received connection response: %s", res_json)

            if res.get("msg") != "connected":
                raise ConnectionError(f"Server rejected connection handshake: {res}")

            self.session_id = uuid.UUID(res.get("session"))
            logger.debug("Established connection: session id %s", self.session_id)
            # authenticate
            auth_msg = {
                "id": self._generate_msg_id(),
                "msg": "method",
                "method": "auth.login",
                "params": [self.username, self._password],
            }
            auth_msg_json = json.dumps(auth_msg)
            logger.debug("Sending authentication request: %s", auth_msg_json)
            await self.websocket.send(auth_msg_json)
            res_json = await self.websocket.recv()
            res = json.loads(res_json)
            logger.debug("Received authentication response: %s", res_json)

            if not res.get("result"):
                logger.error("Authentication failed: %s", res)
                raise AuthenticationError(f"Server rejected authentication")

            logger.info(
                "Successfully connected and authenticated to TrueNAS %s", self.host
            )

        except websockets.exceptions.WebSocketException as e:
            logger.error("Failed to connect to TrueNAS: %s", str(e))
            raise ConnectionError(f"Failed to connect to TrueNAS: {e}")

    async def disconnect(self) -> None:
        """Close WebSocket connection."""
        if self.websocket:
            logger.info("Disconnecting from TrueNAS")
            logger.debug(
                "Session ID %s, processed %s messages",
                self.session_id,
                self._msg_id_counter,
            )
            await self.websocket.close()
            self.websocket = None
            self.session_id = None
            logger.debug("WebSocket connection closed")
        else:
            logger.debug("Disconnect method called but no active connection exists")

    async def _call(self, method: str, params: list) -> TrueNASResponse:
        """Make raw WebSocket API call.

        Args:
            method: API method name (e.g. 'pool.dataset.query')
            params: List of parameters for the method

        Returns:
            TrueNASResponse containing result or error
        """
        if not self.websocket:
            logger.error("Attempted API call with no active connection")
            raise ConnectionError("Not connected")

        message = {
            "id": self._generate_msg_id(),
            "msg": "method",
            "method": method,
            "params": params,
        }

        logger.debug(
            "Sending API call: %s(%s)", method, self._mask_sensitive_params(params)
        )
        await self.websocket.send(json.dumps(message))
        response = await self.websocket.recv()
        parsed = json.loads(response)

        if "error" in parsed and parsed["error"]:
            logger.error("API call %s failed: %s", method, parsed["error"])
        else:
            logger.debug("API call %s succeeded", method)

        return TrueNASResponse(
            id=parsed.get("id"), result=parsed.get("result"), error=parsed.get("error")
        )


class AuthenticationError(Exception):
    pass
