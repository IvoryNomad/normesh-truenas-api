import logging
from typing import Any, Dict, Optional

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class AuditManager:
    """Manages audit operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    audit.config                                        |     No      |         | No
    audit.download_report                               |     No      |         | Yes
    audit.export                                        |     No      |         | Yes
    audit.query                                         |     No      |         | No
    audit.update                                        |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize audit manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...
