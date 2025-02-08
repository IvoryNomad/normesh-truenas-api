from typing import Dict, List, Optional, Union

from .connection import TrueNASConnection, TrueNASResponse


class DatasetManager:
    """Manages ZFS dataset operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    pool.dataset.attachments                            |     No      |         | No
    pool.dataset.change_key                             |     No      |         | Yes
    pool.dataset.checksum_choices                       |     No      |         | No
    pool.dataset.compression_choices                    |     No      |         | No
    pool.dataset.create                                 |     Yes     |  0.1.0  | No
    pool.dataset.delete                                 |     Yes     |  0.1.0  | No
    pool.dataset.destroy_snapshots                      |     No      |         | Yes
    pool.dataset.details                                |     No      |         | No
    pool.dataset.encryption_algorithm_choices           |     No      |         | No
    pool.dataset.encryption_summary                     |     No      |         | Yes
    pool.dataset.export_key                             |     No      |         | Yes
    pool.dataset.export_keys                            |     No      |         | Yes
    pool.dataset.export_keys_for_replication            |     No      |         | Yes
    pool.dataset.get_instance                           |     No      |         | No
    pool.dataset.get_quota                              |     No      |         | No
    pool.dataset.inherit_parent_encryption_properties   |     No      |         | No
    pool.dataset.lock                                   |     No      |         | Yes
    pool.dataset.mountpoint                             |     No      |         | No
    pool.dataset.processes                              |     No      |         | No
    pool.dataset.promote                                |     No      |         | No
    pool.dataset.query                                  |     Yes     |  0.1.0  | No
    pool.dataset.recommended_zvol_blocksize             |     No      |         | No
    pool.dataset.recordsize_choices                     |     No      |         | No
    pool.dataset.set_quota                              |     No      |         | No
    pool.dataset.snapshot_count                         |     No      |         | No
    pool.dataset.unlock                                 |     No      |         | Yes
    pool.dataset.set_quota                              |     No      |         | No
    pool.dataset.unlock_services_restart_choices        |     No      |         | No
    pool.dataset.update                                 |     No      |         | No
    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize dataset manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection

    async def query(
        self, filters: Optional[List] = None, options: Optional[Dict] = None
    ) -> List[Dict]:
        """Query datasets.

        Args:
            filters: List of filters to apply, e.g. [["name", "=", "tank/dataset"]]
            options: Additional query options (count, extra, etc.)

        Returns:
            List of matching datasets
        """
        params = []
        if filters:
            params.append(filters)
        if options:
            params.append(options)

        response = await self.conn._call("pool.dataset.query", params)
        if response.error:
            raise DatasetError(f"Failed to query datasets: {response.error}")
        return response.result

    async def create(
        self,
        name: str,
        type: str = "FILESYSTEM",
        properties: Optional[Dict] = None,
    ) -> Dict:
        """Create a new dataset.

        Args:
            name: Full name of dataset (e.g. "tank/dataset")
            type: Type of dataset ("FILESYSTEM", "VOLUME", etc)
            properties: ZFS properties to set

        Returns:
            Created dataset information

        Raises:
            DatasetError: If creation fails
        """
        params = {"name": name, "type": type}
        if properties:
            params["properties"] = properties

        response = await self.conn._call("pool.dataset.create", [params])
        if response.error:
            raise DatasetError(f"Failed to create dataset: {response.error}")
        return response.result

    async def delete(
        self, name: str, recursive: bool = False, force: bool = False
    ) -> None:
        """Delete a dataset.

        Args:
            name: Name of dataset to delete
            recursive: If True, delete all child datasets
            force: If True, force deletion even if dataset is in use

        Raises:
            DatasetError: If deletion fails
        """
        params = [name, {"recursive": recursive, "force": force}]

        response = await self.conn._call("pool.dataset.delete", params)
        if response.error:
            raise DatasetError(f"Failed to delete dataset: {response.error}")


class DatasetError(Exception):
    """Raised when a dataset operation fails."""

    pass
