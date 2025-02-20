import logging
from typing import Any, Dict, Optional

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class AlertManager:
    """Manages TrueNAS alert operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    alert.dismiss                                       |     No      |         | No
    alert.list                                          |     No      |         | No
    alert.list_categories                               |     No      |         | No
    alert.list_policies                                 |     No      |         | No
    alert.restore                                       |     No      |         | No
    alertclasses.config                                 |     No      |         | No
    alertclasses.update                                 |     No      |         | No
    alertservice.create                                 |     No      |         | No
    alertservice.delete                                 |     No      |         | No
    alertservice.get_instance                           |     No      |         | No
    alertservice.list_types                             |     No      |         | No
    alertservice.query                                  |     No      |         | No
    alertservice.test                                   |     No      |         | No
    alertservice.update                                 |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize job manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...
