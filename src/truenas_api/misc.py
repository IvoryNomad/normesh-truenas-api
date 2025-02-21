import logging
from typing import Any, Dict, Optional

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class DNSManager:
    """Manages DNS operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    dns.query                                           |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize DNS manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...
