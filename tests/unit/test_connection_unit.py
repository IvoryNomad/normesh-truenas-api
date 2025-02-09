import asyncio
import json
import uuid
from unittest.mock import AsyncMock, patch

import pytest

from truenas_api.auth import AuthConfig
from truenas_api.connection import AuthenticationError, TrueNASConnection


@pytest.mark.asyncio
async def test_successful_connection_with_passwd_auth(debug_logging):
    """Test the complete connection process including handshake and password authentication."""
    my_auth_config = AuthConfig(
        auth_type="passwd", username="fakeuser", password="fakepassword"
    )
    conn = TrueNASConnection("truenas.local", my_auth_config)

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
async def test_successful_connection_with_api_key_auth(debug_logging):
    """Test the complete connection process including handshake and password authentication."""
    myapi_key = "1-fJH66ifCpS3yrWhkp3KbIgb7EtiiAHauSnWTthDlo6h4itinLCoY8Xz2HvvFXFDAs"
    my_auth_config = AuthConfig(auth_type="api_key", api_key=myapi_key)
    conn = TrueNASConnection("truenas.local", my_auth_config)

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
        assert auth_msg["method"] == "auth.login_with_api_key"
        assert auth_msg["params"] == [myapi_key]


@pytest.mark.asyncio
async def test_successful_connection_with_token_auth(debug_logging):
    """Test the complete connection process including handshake and password authentication."""
    mytoken = "u6cd04pe1bF8aa9CzCgCmpbQIldvIx3k3C2aNQVdbRLRf2eCYqZVQ9cBZi8r1j7wA"
    my_auth_config = AuthConfig(auth_type="token", token=mytoken)
    conn = TrueNASConnection("truenas.local", my_auth_config)

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
        assert auth_msg["method"] == "auth.login_with_token"
        assert auth_msg["params"] == [mytoken]


@pytest.mark.asyncio
async def test_failed_authentication_with_passwd_auth(debug_logging):
    """Test the complete connection process including handshake and password authentication."""
    my_auth_config = AuthConfig(
        auth_type="passwd", username="fakeuser", password="badpassword"
    )
    conn = TrueNASConnection("truenas.local", my_auth_config)

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
                "result": False,
            }
        ),
    ]

    # Create an AsyncMock for the connect function itself
    mock_connect = AsyncMock(return_value=mock_ws)

    with patch("websockets.connect", mock_connect):
        with pytest.raises(AuthenticationError, match="Server rejected authentication"):
            await conn.connect()


@pytest.mark.asyncio
async def test_failed_authentication_with_api_key_auth(debug_logging):
    """Test the complete connection process including handshake and password authentication."""
    myapi_key = "totally-invalid-api-key"
    my_auth_config = AuthConfig(auth_type="api_key", api_key=myapi_key)
    conn = TrueNASConnection("truenas.local", my_auth_config)

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
                "result": False,
            }
        ),
    ]

    # Create an AsyncMock for the connect function itself
    mock_connect = AsyncMock(return_value=mock_ws)

    with patch("websockets.connect", mock_connect):
        with pytest.raises(AuthenticationError, match="Server rejected authentication"):
            await conn.connect()


@pytest.mark.asyncio
async def test_failed_authentication_with_token_auth(debug_logging):
    """Test the complete connection process including handshake and password authentication."""
    mytoken = "totally-invalid-token"
    my_auth_config = AuthConfig(auth_type="token", token=mytoken)
    conn = TrueNASConnection("truenas.local", my_auth_config)

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
                "result": False,
            }
        ),
    ]

    # Create an AsyncMock for the connect function itself
    mock_connect = AsyncMock(return_value=mock_ws)

    with patch("websockets.connect", mock_connect):
        with pytest.raises(AuthenticationError, match="Server rejected authentication"):
            await conn.connect()


@pytest.mark.asyncio
async def test_failed_handshake(debug_logging):
    """Test handling of a failed handshake response."""
    my_auth_config = AuthConfig(
        auth_type="passwd", username="fakeuser", password="fakepassword"
    )
    conn = TrueNASConnection("truenas.local", my_auth_config)

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
