import logging

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class FTPManager:
    """Manages TrueNAS FTP operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    ftp.config                                          |     No      |         | No
    ftp.update                                          |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize FTP manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class ISCSIManager:
    """Manages TrueNAS iSCSI operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    iscsi.auth.create                                   |     No      |         | No
    iscsi.auth.delete                                   |     No      |         | No
    iscsi.auth.get_instance                             |     No      |         | No
    iscsi.auth.query                                    |     No      |         | No
    iscsi.auth.update                                   |     No      |         | No
    iscsi.extent.create                                 |     No      |         | No
    iscsi.extent.delete                                 |     No      |         | No
    iscsi.extent.disk_choices                           |     No      |         | No
    iscsi.extent.get_instance                           |     No      |         | No
    iscsi.extent.query                                  |     No      |         | No
    iscsi.extent.update                                 |     No      |         | No
    iscsi.global.alua_enabled                           |     No      |         | No
    iscsi.global.config                                 |     No      |         | No
    iscsi.global.sessions                               |     No      |         | No
    iscsi.global.update                                 |     No      |         | No
    iscsi.host.create                                   |     No      |         | No
    iscsi.host.delete                                   |     No      |         | No
    iscsi.host.get_initiators                           |     No      |         | No
    iscsi.host.get_instance                             |     No      |         | No
    iscsi.host.get_targets                              |     No      |         | No
    iscsi.host.query                                    |     No      |         | No
    iscsi.host.set_initiators                           |     No      |         | No
    iscsi.host.set_targets                              |     No      |         | No
    iscsi.host.update                                   |     No      |         | No
    iscsi.initiator.create                              |     No      |         | No
    iscsi.initiator.delete                              |     No      |         | No
    iscsi.initiator.get_instance                        |     No      |         | No
    iscsi.initiator.query                               |     No      |         | No
    iscsi.initiator.update                              |     No      |         | No
    iscsi.portal.create                                 |     No      |         | No
    iscsi.portal.delete                                 |     No      |         | No
    iscsi.portal.get_instance                           |     No      |         | No
    iscsi.portal.listen_ip_choices                      |     No      |         | No
    iscsi.portal.query                                  |     No      |         | No
    iscsi.portal.update                                 |     No      |         | No
    iscsi.target.create                                 |     No      |         | No
    iscsi.target.delete                                 |     No      |         | No
    iscsi.target.get_instance                           |     No      |         | No
    iscsi.target.query                                  |     No      |         | No
    iscsi.target.update                                 |     No      |         | No
    iscsi.targetextent.create                           |     No      |         | No
    iscsi.targetextent.delete                           |     No      |         | No
    iscsi.targetextent.get_instance                     |     No      |         | No
    iscsi.targetextent.query                            |     No      |         | No
    iscsi.targetextent.update                           |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize iSCSI manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class MailManager:
    """Manages TrueNAS Mail operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    mail.config                                         |     No      |         | No
    mail.send                                           |     No      |         | Yes
    mail.update                                         |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize Mail manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


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


class ServiceManager:
    """Manages TrueNAS service operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    service.get_instance                                |     No      |         | No
    service.query                                       |     No      |         | No
    service.reload                                      |     No      |         | No
    service.restart                                     |     No      |         | No
    service.start                                       |     No      |         | No
    service.started                                     |     No      |         | No
    service.started_or_enabled                          |     No      |         | No
    service.stop                                        |     No      |         | No
    service.terminate_process                           |     No      |         | No
    service.update                                      |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize service manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class SMARTManager:
    """Manages TrueNAS SMART operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    smart.config                                        |     No      |         | No
    smart.update                                        |     No      |         | No
    smart.test.abort                                    |     No      |         | No
    smart.test.create                                   |     No      |         | No
    smart.test.delete                                   |     No      |         | No
    smart.test.disk_choices                             |     No      |         | No
    smart.test.get_instance                             |     No      |         | No
    smart.test.manual_test                              |     No      |         | No
    smart.test.query                                    |     No      |         | No
    smart.test.query_for_disk                           |     No      |         | No
    smart.test.results                                  |     No      |         | No
    smart.test.update                                   |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize SMART manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class SMBManager:
    """Manages TrueNAS SMB operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    smb.bindip_choices                                  |     No      |         | No
    smb.client_count                                    |     No      |         | No
    smb.config                                          |     No      |         | No
    smb.domain_choices                                  |     No      |         | No
    smb.status                                          |     No      |         | No
    smb.unixcharset_choices                             |     No      |         | No
    smb.update                                          |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize SMB manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class SNMPManager:
    """Manages TrueNAS SNMP operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    snmp.config                                         |     No      |         | No
    snmp.update                                         |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize SNMP manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class SSHManager:
    """Manages TrueNAS SSH operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    ssh.bindiface_choices                               |     No      |         | No
    ssh.config                                          |     No      |         | No
    ssh.update                                          |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize SSH manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class UPSManager:
    """Manages TrueNAS UPS operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    ups.config                                          |     No      |         | No
    ups.driver_choices                                  |     No      |         | No
    ups.port_choices                                    |     No      |         | No
    ups.update                                          |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize UPS manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
