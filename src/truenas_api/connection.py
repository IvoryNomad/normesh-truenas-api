import asyncio
import websockets
import json
from typing import Optional, Dict, Any
from dataclasses import dataclass


@dataclass
class TrueNASResponse:
    id: str
    result: Any
    error: Optional[Dict]


class TrueNASConnection:
    def __init__(self, host: str, api_key: str):
        """Initialize TrueNAS connection.

        Args:
            host: TrueNAS hostname/IP (e.g. 'truenas.local')
            api_key: API key for authentication
        """
        self.host = host
        self.api_key = api_key
        self.websocket = None
        self.connection_id = None
        self._msg_id = 0  # For tracking API calls

    async def connect(self) -> None:
        """Establish WebSocket connection to TrueNAS.

        Raises:
            ConnectionError: If connection cannot be established
            AuthenticationError: If API key is invalid
        """
        uri = f"ws://{self.host}/websocket"
        try:
            self.websocket = await websockets.connect(uri)
            # Send authentication message
            auth_response = await self._call("auth.login", [self.api_key])
            if not auth_response.result:
                raise AuthenticationError("Invalid API key")
        except websockets.exceptions.WebSocketException as e:
            raise ConnectionError(f"Failed to connect to TrueNAS: {e}")

    async def disconnect(self) -> None:
        """Close WebSocket connection."""
        if self.websocket:
            await self.websocket.close()
            self.websocket = None
            self.connection_id = None

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

        self._msg_id += 1
        message = {
            "id": str(self._msg_id),
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
