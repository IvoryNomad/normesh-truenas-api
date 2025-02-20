import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Awaitable, Callable, Literal, Optional

from .connection import TrueNASConnection, TrueNASResponse

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


class AcmeDNSAuthManager:
    """Manages ACME DNS authentication operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    acme.dns.authenticator.authenticator_schemas        |     No      |         | No
    acme.dns.authenticator.create                       |     No      |         | No
    acme.dns.authenticator.delete                       |     No      |         | No
    acme.dns.authenticator.get_instance                 |     No      |         | No
    acme.dns.authenticator.query                        |     No      |         | No
    acme.dns.authenticator.update                       |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize acme-dns authenticator manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class ActiveDirectoryManager:
    """Manages ActiveDirectory authentication operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    activedirectory.config                              |     No      |         | No
    activedirectory.domain_info                         |     No      |         | No
    activedirectory.leave                               |     No      |         | Yes
    activedirectory.nss_info_choices                    |     No      |         | No
    activedirectory.update                              |     No      |         | Yes

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize ActiveDirectory manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class APIKeyManager:
    """Manages API Key operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    api_key.create                                      |     No      |         | No
    api_key.delete                                      |     No      |         | No
    api_key.get_instance                                |     No      |         | No
    api_key.query                                       |     No      |         | No
    api_key.update                                      |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize API Key manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class AuthManager:
    """Manages authentication operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    auth.check_password                                 |     No      |         | No
    auth.check_user                                     |     No      |         | No
    auth.generate_token                                 |     No      |         | No
    auth.login                                          |     Yes*    |  0.1.0  | No
    auth.login_with_api_key                             |     Yes*    |  0.1.0  | No
    auth.login_with_token                               |     Yes*    |  0.1.0  | No
    auth.logout                                         |     No      |         | No
    auth.me                                             |     No      |         | No
    auth.sessions                                       |     No      |         | No
    auth.set_attributes                                 |     No      |         | No
    auth.terminate_other_sessions                       |     No      |         | No
    auth.two_factor_auth                                |     No      |         | No
    auth.twofactor.config                               |     No      |         | No
    auth.twofactor.update                               |     No      |         | No

    * Note: auth.login methods implemented in AuthStrategy and called in
            TrueNASConnection.connect

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize authentication manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class DirectorySvcManager:
    """Manages directory services operations via TrueNAS WebSocket API

     Available methods                                   | implemented | planned | Job?
     ----------------------------------------------------+-------------+---------+------
    directoryservices.get_state                          |     No      |         | No
    directoryservices.status                             |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize directory services manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...
