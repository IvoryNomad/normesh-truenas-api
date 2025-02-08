import asyncio
import json
import uuid
from unittest.mock import AsyncMock, patch

import pytest

from truenas_api.connection import AuthenticationError, TrueNASConnection


@pytest.mark.asyncio
async def test_successful_connection_with_handshake():
    """Test the complete connection process including handshake and authentication."""
    conn = TrueNASConnection("truenas.local", "fakeuser", "fakepassword")

    # Create our mock websocket
    mock_ws = AsyncMock()
    session_id = uuid.UUID("b4a4d164-6bc7-11e6-8a93-00e04d680384")

    # Set up the responses for the websocket
    mock_ws.recv.side_effect = [
        # First response - handshake
        json.dumps({"msg": "connected", "session": str(session_id)}),
        # Second response - authentication
        json.dumps(
            {
                "id": str(uuid.uuid5(session_id, str(1))),
                "msg": "result",
                "result": True,
            }
        ),
    ]

    # Create an AsyncMock for the connect function itself
    mock_connect = AsyncMock(return_value=mock_ws)

    # Patch the connect function
    with patch("websockets.connect", mock_connect):
        await conn.connect()

        # Verify connection state
        assert conn.websocket is not None
        assert conn.session_id == session_id

        # Verify the messages we sent were correct
        calls = mock_ws.send.call_args_list
        assert len(calls) == 2  # Should have sent handshake and auth messages

        # Check handshake message
        handshake_msg = json.loads(calls[0].args[0])
        assert handshake_msg == {"msg": "connect", "version": "1", "support": ["1"]}

        # Check auth message
        auth_msg = json.loads(calls[1].args[0])
        assert auth_msg["id"] == str(uuid.uuid5(session_id, str(1)))
        assert auth_msg["msg"] == "method"
        assert auth_msg["method"] == "auth.login"
        assert auth_msg["params"] == ["fakeuser", "fakepassword"]


@pytest.mark.asyncio
async def test_failed_handshake():
    """Test handling of a failed handshake response."""
    conn = TrueNASConnection("truenas.local", "fakeuser", "fakepassword")

    mock_ws = AsyncMock()
    mock_ws.recv.return_value = json.dumps(
        {"msg": "failed", "error": "Unsupported version"}
    )

    mock_connect = AsyncMock(return_value=mock_ws)

    with patch("websockets.connect", mock_connect):
        with pytest.raises(
            ConnectionError, match="Server rejected connection handshake"
        ):
            await conn.connect()


@pytest.mark.asyncio
async def test_failed_authentication():
    """Test handling of failed authentication."""
    conn = TrueNASConnection("truenas.local", "fakeuser", "wrongpassword")

    test_session = uuid.uuid4()
    mock_ws = AsyncMock()
    mock_ws.recv.side_effect = [
        # First response - successful handshake
        json.dumps({"msg": "connected", "session": str(test_session)}),
        # Second response - auth failure
        json.dumps(
            {
                "id": str(uuid.uuid5(test_session, str(1))),
                "msg": "result",
                "result": False,
            }
        ),
    ]

    mock_connect = AsyncMock(return_value=mock_ws)

    with patch("websockets.connect", mock_connect):
        with pytest.raises(AuthenticationError, match="Server rejected authentication"):
            await conn.connect()
