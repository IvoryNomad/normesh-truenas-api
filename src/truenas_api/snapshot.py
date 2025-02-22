import logging
from typing import Any, Dict, Optional

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class SnapshotTaskManager:
    """Manages TrueNAS snapshot task operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    pool.snapshottask.create                            |     No      |         | No
    pool.snapshottask.delete                            |     No      |         | No
    pool.snapshottask.delete_will_change_retention_for  |     No      |         | No
    pool.snapshottask.foreseen_count                    |     No      |         | No
    pool.snapshottask.get_instance                      |     No      |         | No
    pool.snapshottask.max_count                         |     No      |         | No
    pool.snapshottask.max_total_count                   |     No      |         | No
    pool.snapshottask.query                             |     No      |         | No
    pool.snapshottask.run                               |     No      |         | No
    pool.snapshottask.update                            |     No      |         | No
    pool.snapshottask.update_will_change_retention_for  |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize snapshot task manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class SnapshotManager:
    """Manages TrueNAS snapshot operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    zfs.snapshot.clone                                  |     No      |         | No
    zfs.snapshot.create                                 |     No      |         | No
    zfs.snapshot.delete                                 |     No      |         | No
    zfs.snapshot.get_instance                           |     No      |         | No
    zfs.snapshot.hold                                   |     No      |         | No
    zfs.snapshot.query                                  |     No      |         | No
    zfs.snapshot.release                                |     No      |         | No
    zfs.snapshot.remove                                 |     No      |         | No
    zfs.snapshot.rollback                               |     No      |         | No
    zfs.snapshot.update                                 |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize snapshot manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
