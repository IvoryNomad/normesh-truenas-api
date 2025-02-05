import pytest
import json
import asyncio
from unittest.mock import AsyncMock, patch
from truenas_api.connection import TrueNASConnection, AuthenticationError


#@pytest.mark.integration
@pytest.mark.asyncio
async def test_live_connection():
    """Test connection to actual TrueNAS instance.

    Requires environment variables:
        TRUENAS_HOST: Hostname/IP of TrueNAS instance
        TRUENAS_USERNAME: API user username
        TRUENAS_PASSWORD: API user password
    """
    import os

    host = os.getenv("TRUENAS_HOST")
    username = os.getenv("TRUENAS_USERNAME")
    password = os.getenv("TRUENAS_PASSWORD")

    if not all([host, username, password]):
        pytest.skip("Missing required environment variables for live testing")

    conn = TrueNASConnection(host, username, password)
    await conn.connect()
    assert conn.websocket is not None
    await conn.disconnect()
