import logging
from typing import Any, Dict, Optional

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class CoreManager:
    """Manages TrueNAS core operations

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    core.arp                                            |     No      |  0.1.0  | No
    core.bulk                                           |     No      |         | Yes
    core.debug                                          |     No      |         | No
    core.debug_mode_enabled                             |     No      |         | No
    core.download                                       |     No      |  0.1.0  | No
    core.get_events                                     |     No      |         | No
    core.ping                                           |     No      |  0.1.0  | No
    core.ping_remote                                    |     No      |  0.1.0  | No
    core.resize_shell                                   |     No      |         | No
    core.sessions                                       |     No      |         | No
    core.set_debug_mode                                 |     No      |         | No

    The following methods either are or will be implemented in jobs.JobManager:
    - core.download_jobs
    - core.get_jobs
    - core.job_abort
    - core.job_wait
    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize job manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
