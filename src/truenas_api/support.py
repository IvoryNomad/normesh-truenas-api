import logging

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class SupportManager:
    """Manages TrueNAS support operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    support.attach_ticket                               |     No      |         | Yes
    support.attach_ticket_max_size                      |     No      |         | No
    support.config                                      |     No      |         | No
    support.fetch_categories                            |     No      |         | No
    support.fields                                      |     No      |         | No
    support.is_available                                |     No      |         | No
    support.is_available_and_enabled                    |     No      |         | No
    support.new_ticket                                  |     No      |         | Yes
    support.similar_issues                              |     No      |         | No
    support.update                                      |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize support manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
