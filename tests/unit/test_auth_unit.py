import uuid
from unittest.mock import AsyncMock, patch

import pytest

from truenas_api.auth import (ApiKeyAuth, AuthConfig, PasswordAuth, TokenAuth,
                              create_auth_strategy)
from truenas_api.connection import TrueNASResponse


# Test AuthConfig validation
def test_auth_config_password():
    """Test creating AuthConfig for password authentication."""
    config = AuthConfig(
        auth_type='passwd',
        username='testuser',
        password='testpass'
    )
    assert config.auth_type == 'passwd'
    assert config.username == 'testuser'
    assert config.password == 'testpass'

def test_auth_config_api_key():
    """Test creating AuthConfig for API key authentication."""
    config = AuthConfig(
        auth_type='api_key',
        api_key='testkey123'
    )
    assert config.auth_type == 'api_key'
    assert config.api_key == 'testkey123'

def test_auth_config_token():
    """Test creating AuthConfig for token authentication."""
    config = AuthConfig(
        auth_type='token',
        token='testtoken123'
    )
    assert config.auth_type == 'token'
    assert config.token == 'testtoken123'

def test_auth_config_invalid_type():
    """Test that invalid auth_type raises ValueError."""
    with pytest.raises(ValueError):
        create_auth_strategy(AuthConfig(auth_type='invalid'))

def test_auth_config_missing_credentials():
    """Test that missing credentials raise ValueError."""
    with pytest.raises(ValueError):
        create_auth_strategy(AuthConfig(auth_type='passwd'))
    
    with pytest.raises(ValueError):
        create_auth_strategy(AuthConfig(auth_type='api_key'))
    
    with pytest.raises(ValueError):
        create_auth_strategy(AuthConfig(auth_type='token'))

# Test Authentication Strategies
@pytest.mark.asyncio
async def test_password_auth_success():
    """Test successful password authentication."""
    auth = PasswordAuth('testuser', 'testpass')
    mock_call = AsyncMock(return_value=TrueNASResponse(
        id='1',
        result=True,
        error=None
    ))
    
    success = await auth.authenticate(mock_call)
    assert success is True
    
    mock_call.assert_called_once_with(
        'auth.login',
        ['testuser', 'testpass']
    )

@pytest.mark.asyncio
async def test_password_auth_failure():
    """Test failed password authentication."""
    auth = PasswordAuth('testuser', 'wrongpass')
    mock_call = AsyncMock(return_value=TrueNASResponse(
        id='1',
        result=False,
        error=None
    ))
    
    success = await auth.authenticate(mock_call)
    assert success is False

@pytest.mark.asyncio
async def test_api_key_auth_success():
    """Test successful API key authentication."""
    auth = ApiKeyAuth('testkey123')
    mock_call = AsyncMock(return_value=TrueNASResponse(
        id='1',
        result=True,
        error=None
    ))
    
    success = await auth.authenticate(mock_call)
    assert success is True
    
    mock_call.assert_called_once_with(
        'auth.login_with_api_key',
        ['testkey123']
    )

@pytest.mark.asyncio
async def test_api_key_auth_failure():
    """Test failed API key authentication."""
    auth = ApiKeyAuth('wrongkey')
    mock_call = AsyncMock(return_value=TrueNASResponse(
        id='1',
        result=False,
        error=None
    ))
    
    success = await auth.authenticate(mock_call)
    assert success is False

@pytest.mark.asyncio
async def test_token_auth_success():
    """Test successful token authentication."""
    auth = TokenAuth('testtoken123')
    mock_call = AsyncMock(return_value=TrueNASResponse(
        id='1',
        result=True,
        error=None
    ))
    
    success = await auth.authenticate(mock_call)
    assert success is True
    
    mock_call.assert_called_once_with(
        'auth.login_with_token',
        ['testtoken123']
    )

@pytest.mark.asyncio
async def test_token_auth_failure():
    """Test failed token authentication."""
    auth = TokenAuth('wrongtoken')
    mock_call = AsyncMock(return_value=TrueNASResponse(
        id='1',
        result=False,
        error=None
    ))
    
    success = await auth.authenticate(mock_call)
    assert success is False

# Test Strategy Creation
def test_create_password_strategy():
    """Test creating password authentication strategy."""
    config = AuthConfig(
        auth_type='passwd',
        username='testuser',
        password='testpass'
    )
    strategy = create_auth_strategy(config)
    assert isinstance(strategy, PasswordAuth)
    assert strategy.username == 'testuser'
    assert strategy.password == 'testpass'

def test_create_api_key_strategy():
    """Test creating API key authentication strategy."""
    config = AuthConfig(
        auth_type='api_key',
        api_key='testkey123'
    )
    strategy = create_auth_strategy(config)
    assert isinstance(strategy, ApiKeyAuth)
    assert strategy.api_key == 'testkey123'

def test_create_token_strategy():
    """Test creating token authentication strategy."""
    config = AuthConfig(
        auth_type='token',
        token='testtoken123'
    )
    strategy = create_auth_strategy(config)
    assert isinstance(strategy, TokenAuth)
    assert strategy.token == 'testtoken123'