import logging

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class NFSManager:
    """Manages TrueNAS NFS operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    nfs.bindip_choices                                  |     No      |         | No
    nfs.client_count                                    |     No      |         | No
    nfs.config                                          |     No      |         | No
    nfs.get_nfs3_clients                                |     No      |         | No
    nfs.get_nfs4_clients                                |     No      |         | No
    nfs.update                                          |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize NFS manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
