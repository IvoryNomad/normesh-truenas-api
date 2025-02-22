import logging

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class CloudReplicationManager:
    """Manages cloud replication operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    cloud_backup.abort                                  |     No      |         | No
    cloud_backup.create                                 |     No      |         | No
    cloud_backup.delete                                 |     No      |         | No
    cloud_backup.delete_snapshot                        |     No      |         | Yes
    cloud_backup.get_instance                           |     No      |         | No
    cloud_backup.list_snapshot_directory                |     No      |         | No
    cloud_backup.list_snapshots                         |     No      |         | No
    cloud_backup.query                                  |     No      |         | No
    cloud_backup.restore                                |     No      |         | Yes
    cloud_backup.sync                                   |     No      |         | Yes
    cloud_backup.transfer_setting_choices               |     No      |         | No
    cloud_backup.update                                 |     No      |         | No
    cloudsync.abort                                     |     No      |         | No
    cloudsync.create                                    |     No      |         | No
    cloudsync.create_bucket                             |     No      |         | No
    cloudsync.delete                                    |     No      |         | No
    cloudsync.get_instance                              |     No      |         | No
    cloudsync.list_buckets                              |     No      |         | No
    cloudsync.list_directory                            |     No      |         | No
    cloudsync.providers                                 |     No      |         | No
    cloudsync.query                                     |     No      |         | No
    cloudsync.restore                                   |     No      |         | No
    cloudsync.sync                                      |     No      |         | Yes
    cloudsync.sync_onetime                              |     No      |         | Yes
    cloudsync.update                                    |     No      |         | No
    cloudsync.credentials.create                        |     No      |         | No
    cloudsync.credentials.delete                        |     No      |         | No
    cloudsync.credentials.get_instance                  |     No      |         | No
    cloudsync.credentials.query                         |     No      |         | No
    cloudsync.credentials.update                        |     No      |         | No
    cloudsync.credentials.verify                        |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize cloud replication manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class ReplicationManager:
    """Manages TrueNAS replication operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    replication.count_eligible_manual_snapshots         |     No      |         | No
    replication.create                                  |     No      |         | No
    replication.create_dataset                          |     No      |         | No
    replication.delete                                  |     No      |         | No
    replication.get_instance                            |     No      |         | No
    replication.list_datasets                           |     No      |         | No
    replication.list_naming_schemas                     |     No      |         | No
    replication.query                                   |     No      |         | No
    replication.restore                                 |     No      |         | No
    replication.run                                     |     No      |         | Yes
    replication.run_onetime                             |     No      |         | Yes
    replication.target_unmatched_snapshots              |     No      |         | No
    replication.update                                  |     No      |         | No
    replication.config.config                           |     No      |         | No
    replication.config.update                           |     No      |         | No

    """


class RsyncTaskManager:
    """Manages TrueNAS rsync task operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    rsynctask.create                                    |     No      |         | No
    rsynctask.delete                                    |     No      |         | No
    rsynctask.get_instance                              |     No      |         | No
    rsynctask.query                                     |     No      |         | No
    rsynctask.run                                       |     No      |         | Yes
    rsynctask.update                                    |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize rsync task manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
