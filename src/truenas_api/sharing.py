import logging

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class NFSShareManager:
    """Manages TrueNAS NFS share operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    sharing.nfs.create                                  |     No      |         | No
    sharing.nfs.delete                                  |     No      |         | No
    sharing.nfs.get_instance                            |     No      |         | No
    sharing.nfs.query                                   |     No      |         | No
    sharing.nfs.update                                  |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize NFS share manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class SMBShareManager:
    """Manages TrueNAS SMB share operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    sharing.smb.create                                  |     No      |         | No
    sharing.smb.delete                                  |     No      |         | No
    sharing.smb.get_instance                            |     No      |         | No
    sharing.smb.getacl                                  |     No      |         | No
    sharing.smb.presets                                 |     No      |         | No
    sharing.smb.query                                   |     No      |         | No
    sharing.smb.setacl                                  |     No      |         | No
    sharing.smb.update                                  |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize SMB share manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
