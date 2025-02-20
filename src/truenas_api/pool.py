import logging
from typing import Dict, List, Optional, Union

from .connection import TrueNASConnection, TrueNASResponse
from .job import JobManager

# Create module logger
logger = logging.getLogger(__name__)


class PoolManager:
    """Manages ZFS dataset operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    pool.attach                                         |     No      |         | Yes
    pool.attachments                                    |     No      |         | No
    pool.create                                         |     No      |  0.1.0  | Yes
    pool.detach                                         |     No      |         | No
    pool.expand                                         |     No      |         | Yes
    pool.export                                         |     No      |         | Yes
    pool.filesystem_choices                             |     No      |  0.1.0  | No
    pool.get_disks                                      |     No      |  0.1.0  | No
    pool.get_instance                                   |     No      |  0.1.0  | No
    pool.get_instance_by_name                           |     No      |  0.1.0  | No
    pool.import_find                                    |     No      |         | Yes
    pool.import_pool                                    |     No      |         | Yes
    pool.is_upgraded                                    |     No      |  0.1.0  | No
    pool.offline                                        |     No      |  0.1.0  | No
    pool.online                                         |     No      |  0.1.0  | No
    pool.processes                                      |     No      |         | No
    pool.query                                          |     No      |  0.1.0  | No
    pool.remove                                         |     No      |         | Yes
    pool.replace                                        |     No      |         | Yes
    pool.scrub                                          |     No      |         | Yes
    pool.update                                         |     No      |         | Yes
    pool.upgrade                                        |     No      |  0.1.0  | No
    pool.validate_name                                  |     No      |  0.1.0  | No
    pool.resilver.config                                |     No      |         | No
    pool.resilver.update                                |     No      |         | No
    pool.scrub.create                                   |     No      |         | No
    pool.scrub.delete                                   |     No      |         | No
    pool.scrub.get_instance                             |     No      |         | No
    pool.scrub.query                                    |     No      |         | No
    pool.scrub.run                                      |     No      |         | No
    pool.scrub.scrub                                    |     No      |         | Yes
    pool.scrub.update                                   |     No      |         | No
    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize pool manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        self.job_mgr = JobManager(connection)

    async def create(): ...
