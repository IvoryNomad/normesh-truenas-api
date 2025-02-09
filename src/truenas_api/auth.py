import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Literal, Optional

logger = logging.getLogger(__name__)


@dataclass
class AuthConfig:
    """Configuration for TrueNAS authentication."""

    auth_type: Literal["passwd", "api_key", "token"]
    username: Optional[str] = None  # Only needed for password auth
    password: Optional[str] = None
    api_key: Optional[str] = None
    token: Optional[str] = None


class AuthStrategy(ABC):
    """Abstract base class for authentication strategies."""

    @abstractmethod
    async def authenticate(
        self, call_method: Callable[[str, list], Awaitable[Any]]
    ) -> bool:
        """Perform authentication using the provided call method."""
        ...  # pragma: no cover


class PasswordAuth(AuthStrategy):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    async def authenticate(self, call_method) -> bool:
        response = await call_method("auth.login", [self.username, self.password])
        return bool(response.result)


class ApiKeyAuth(AuthStrategy):
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def authenticate(self, call_method) -> bool:
        response = await call_method("auth.login_with_api_key", [self.api_key])
        return bool(response.result)


class TokenAuth(AuthStrategy):
    def __init__(self, token: str):
        self.token = token

    async def authenticate(self, call_method) -> bool:
        response = await call_method("auth.login_with_token", [self.token])
        return bool(response.result)


def create_auth_strategy(config: AuthConfig) -> AuthStrategy:
    """Factory function to create appropriate auth strategy."""
    if config.auth_type == "passwd":
        if not config.username or not config.password:
            raise ValueError(
                "Username and password required for password authentication"
            )
        return PasswordAuth(config.username, config.password)
    elif config.auth_type == "api_key":
        if not config.api_key:
            raise ValueError("API key required for API key authentication")
        return ApiKeyAuth(config.api_key)
    elif config.auth_type == "token":
        if not config.token:
            raise ValueError("Token required for token authentication")
        return TokenAuth(config.token)
    else:
        raise ValueError(f"Unsupported auth type: {config.auth_type}")
