import logging

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class VMwareManager:
    """Manages TrueNAS vmware operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    vmware.create                                       |     No      |         | No
    vmware.dataset_has_vms                              |     No      |         | No
    vmware.delete                                       |     No      |         | No
    vmware.get_datastores                               |     No      |         | No
    vmware.get_instance                                 |     No      |         | No
    vmware.get_virtual_machines                         |     No      |         | No
    vmware.match_datastores_with_datasets               |     No      |         | No
    vmware.query                                        |     No      |         | No
    vmware.update                                       |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize vmware manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
