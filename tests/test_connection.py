# tests/test_connection.py
import pytest
import asyncio
from unittest.mock import Mock, patch
from truenas.connection import TrueNASConnection, AuthenticationError


@pytest.fixture
async def truenas_conn():
    """Create a TrueNASConnection instance for testing."""
    conn = TrueNASConnection("truenas.local", "fake-api-key")
    yield conn
    # Cleanup
    await conn.disconnect()


@pytest.mark.asyncio
async def test_successful_connection(truenas_conn):
    """Test successful connection and authentication."""
    with patch("websockets.connect") as mock_connect:
        # Create mock websocket
        mock_ws = Mock()
        mock_ws.send = asyncio.coroutine(lambda x: None)
        mock_ws.recv = asyncio.coroutine(lambda: '{"id": "1", "result": true}')
        mock_connect.return_value = mock_ws

        await truenas_conn.connect()
        assert truenas_conn.websocket is not None


@pytest.mark.asyncio
async def test_failed_authentication(truenas_conn):
    """Test handling of invalid API key."""
    with patch("websockets.connect") as mock_connect:
        mock_ws = Mock()
        mock_ws.send = asyncio.coroutine(lambda x: None)
        mock_ws.recv = asyncio.coroutine(
            lambda: '{"id": "1", "result": false, "error": "Invalid API key"}'
        )
        mock_connect.return_value = mock_ws

        with pytest.raises(AuthenticationError):
            await truenas_conn.connect()


# For testing against real TrueNAS instance
@pytest.mark.integration
@pytest.mark.asyncio
async def test_live_connection():
    """Test connection to actual TrueNAS instance.

    Requires environment variables:
        TRUENAS_HOST: Hostname/IP of TrueNAS instance
        TRUENAS_API_KEY: Valid API key
    """
    import os

    host = os.getenv("TRUENAS_HOST")
    api_key = os.getenv("TRUENAS_API_KEY")

    if not all([host, api_key]):
        pytest.skip("Missing required environment variables for live testing")

    conn = TrueNASConnection(host, api_key)
    await conn.connect()
    assert conn.websocket is not None
    await conn.disconnect()
