import asyncio
import json
from unittest.mock import AsyncMock, patch

import pytest

from truenas_api.auth import AuthConfig
from truenas_api.connection import AuthenticationError, TrueNASConnection


@pytest.mark.integration
@pytest.mark.asyncio
async def test_live_connection_with_passwd():
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

    my_auth_config = AuthConfig(
        auth_type="passwd", username=username, password=password
    )
    conn = TrueNASConnection(host, my_auth_config)
    await conn.connect()
    assert conn.websocket is not None
    await conn.disconnect()
