import asyncio
import json
import uuid
from dataclasses import dataclass
from typing import Any, Dict, Optional

import websockets


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

    def _generate_msg_id(self) -> str:
        """Generate a unique msg id for this message.

        Increments _msg_id_counter

        Returns: UUID
        """
        self._msg_id_counter += 1
        return str(uuid.uuid5(self.session_id, str(self._msg_id_counter)))

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
        try:
            # open the websocket
            self.websocket = await websockets.connect(uri)
            # establish connection
            conn_msg = {"msg": "connect", "version": "1", "support": ["1"]}
            await self.websocket.send(json.dumps(conn_msg))
            res_json = await self.websocket.recv()
            res = json.loads(res_json)

            if res.get("msg") != "connected":
                raise ConnectionError(f"Server rejected connection handshake: {res}")

            self.session_id = uuid.UUID(res.get("session"))
            # authenticate
            auth_msg = {
                "id": self._generate_msg_id(),
                "msg": "method",
                "method": "auth.login",
                "params": [self.username, self._password],
            }
            await self.websocket.send(json.dumps(auth_msg))
            res_json = await self.websocket.recv()
            res = json.loads(res_json)

            if not res.get("result"):
                raise AuthenticationError(f"Server rejected authentication: {res}")
        except websockets.exceptions.WebSocketException as e:
            raise ConnectionError(f"Failed to connect to TrueNAS: {e}")

    async def disconnect(self) -> None:
        """Close WebSocket connection."""
        if self.websocket:
            await self.websocket.close()
            self.websocket = None
            self.session_id = None

    async def _call(self, method: str, params: list) -> TrueNASResponse:
        """Make raw WebSocket API call.

        Args:
            method: API method name (e.g. 'pool.dataset.query')
            params: List of parameters for the method

        Returns:
            TrueNASResponse containing result or error
        """
        if not self.websocket:
            raise ConnectionError("Not connected")

        message = {
            "id": self._generate_msg_id(),
            "msg": "method",
            "method": method,
            "params": params,
        }

        await self.websocket.send(json.dumps(message))
        response = await self.websocket.recv()
        parsed = json.loads(response)

        return TrueNASResponse(
            id=parsed.get("id"), result=parsed.get("result"), error=parsed.get("error")
        )


class AuthenticationError(Exception):
    pass
