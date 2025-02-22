import logging

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class TrueCommandManager:
    """Manages TrueNAS TrueCommand operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    truecommand.config                                  |     No      |         | No
    truecommand.info                                    |     No      |         | No
    truecommand.update                                  |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize TrueCommand manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
