import logging
from typing import Any, Dict, List, Literal, Optional, Union

from .connection import TrueNASConnection, TrueNASResponse

# Create module logger
logger = logging.getLogger(__name__)


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
    pool.dataset.get_instance                           |     Yes     |  0.1.0  | No
    pool.dataset.get_quota                              |     Yes     |  0.1.0  | No
    pool.dataset.inherit_parent_encryption_properties   |     No      |         | No
    pool.dataset.lock                                   |     No      |         | Yes
    pool.dataset.mountpoint                             |     No      |         | No
    pool.dataset.processes                              |     No      |         | No
    pool.dataset.promote                                |     No      |         | No
    pool.dataset.query                                  |     Yes     |  0.1.0  | No
    pool.dataset.recommended_zvol_blocksize             |     No      |         | No
    pool.dataset.recordsize_choices                     |     No      |         | No
    pool.dataset.set_quota                              |     No      |  0.1.0  | No
    pool.dataset.snapshot_count                         |     No      |         | No
    pool.dataset.unlock                                 |     No      |         | Yes
    pool.dataset.unlock_services_restart_choices        |     No      |         | No
    pool.dataset.update                                 |     No      |  0.1.0  | No
    pool.dataset.userprop.create                        |     No      |         | No
    pool.dataset.userprop.delete                        |     No      |         | No
    pool.dataset.userprop.get_instance                  |     No      |         | No
    pool.dataset.userprop.query                         |     No      |         | No
    pool.dataset.userprop.update                        |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize dataset manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection

    async def create(
        self,
        name: str,
        type: Literal["FILESYSTEM", "VOLUME"] = "FILESYSTEM",
        properties: Optional[Dict] = None,
        create_ancestors: bool = False,
        encryption: bool = False,
        inherit_encryption: bool = True,
        encryption_options: Optional[Dict] = None,
        share_type: Literal[
            "GENERIC", "MULTIPROTOCOL", "NFS", "SMB", "APPS"
        ] = "GENERIC",
    ) -> Dict:
        """Create a new dataset.

        Args:
            name: Full name of dataset (e.g. "tank/dataset")
            type: Type of dataset ("FILESYSTEM" or "VOLUME")
            properties: Dataset properties to set. For VOLUME type, 'volsize' is required.
                       Common properties include:
                       - compression: "ON", "OFF", "LZ4", "GZIP", etc.
                       - sync: "STANDARD", "ALWAYS", "DISABLED"
                       - acltype: "OFF", "NFSV4", "POSIX"
                       Most properties can also be set to "INHERIT"
            create_ancestors: Create parent datasets if they don't exist
            encryption: Enable ZFS encryption for this dataset
            inherit_encryption: Inherit encryption settings from parent
            encryption_options: Encryption settings if encryption=True. Keys:
                              - generate_key: bool
                              - algorithm: "AES-256-GCM" etc.
                              - passphrase: str
                              - key: str
            share_type: Type of share this dataset will be used for

        Returns:
            Created dataset information

        Raises:
            DatasetError: If creation fails or parameters are invalid
        """
        logger.debug("Creating dataset %s of type %s", name, type)

        params = {
            "name": name,
            "type": type,
            "create_ancestors": create_ancestors,
            "encryption": encryption,
            "inherit_encryption": inherit_encryption,
            "share_type": share_type,
        }

        if encryption_options:
            params["encryption_options"] = encryption_options

        # Validate VOLUME requirements
        if type == "VOLUME":
            if not properties or "volsize" not in properties:
                logger.error("Missing required volsize for VOLUME creation")
                raise DatasetError("volsize required for VOLUME type")
            if "volblocksize" in properties and properties["volblocksize"] not in [
                "512",
                "512B",
                "1K",
                "2K",
                "4K",
                "8K",
                "16K",
                "32K",
                "64K",
                "128K",
            ]:
                logger.error("Invalid volblocksize: %s", properties["volblocksize"])
                raise DatasetError("Invalid volblocksize")

        # Add and validate properties
        if properties:
            logger.debug("Adding properties: %s", properties)
            # Could add property validation here
            params.update(properties)

        logger.debug("Calling pool.dataset.create with params %s", params)
        response = await self.conn._call("pool.dataset.create", [params])
        if response.error:
            logger.error("Failed to create dataset: %s", response.error)
            raise DatasetError(f"Failed to create dataset: {response.error}")

        logger.info("Successfully created dataset %s", name)
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

        logger.debug("Calling pool.dataset.delete with params %s", params)
        response = await self.conn._call("pool.dataset.delete", params)
        if response.error:
            logger.error("Failed to delete dataset: %s", response.error)
            raise DatasetError(f"Failed to delete dataset: {response.error}")

        # shouldn't we return true here?

    async def get_instance(
        self,
        id: Union[str, bool, dict, list],
        relationships: bool = True,
        extend: Optional[str] = None,
        extend_context: Optional[str] = None,
        prefix: Optional[str] = None,
        extra: Dict = None,
        order_by: list = None,
        select: list = None,
        count: bool = False,
        get: bool = False,
        offset: int = 0,
        limit: int = 0,
        force_sql_filters: bool = True,
    ) -> Dict:
        """Get a specific dataset instance.

        Args:
            id: Identifier for the dataset to retrieve. Can be a string (name),
                integer, boolean, dict, or list.
            relationships: Whether to include relationships (default: True)
            extend: Extension key (default: None)
            extend_context: Extension context (default: None)
            prefix: Prefix filter (default: None)
            extra: Additional parameters (default: {})
            order_by: Sort fields (default: [])
            select: Fields to select (default: [])
            count: Return count only (default: False)
            get: Return single object (default: False)
            offset: Query offset (default: 0)
            limit: Query limit (default: 0)
            force_sql_filters: Force SQL filtering (default: True)

        Returns:
            Dict containing dataset information

        Raises:
            DatasetError: If dataset is not found or other error occurs
            NotImplementedError: If id is a boolean (support not yet implemented)
        """
        # Safety check for boolean ids
        if isinstance(id, bool):
            logger.warning("Boolean dataset ids are not currently supported")
            raise NotImplementedError(
                "Boolean values for dataset id are not currently supported"
            )

        logger.debug("Getting dataset instance for id: %s", id)

        # Build options dict with non-None values
        options = {
            "relationships": relationships,
            "extend": extend,
            "extend_context": extend_context,
            "prefix": prefix,
            "extra": extra or {},
            "order_by": order_by or [],
            "select": select or [],
            "count": count,
            "get": get,
            "offset": offset,
            "limit": limit,
            "force_sql_filters": force_sql_filters,
        }

        # Remove None values
        options = {k: v for k, v in options.items() if v is not None}

        logger.debug("Query options: %s", options)

        response = await self.conn._call("pool.dataset.get_instance", [id, options])
        if response.error:
            logger.error("Failed to get dataset instance: %s", response.error)
            raise DatasetError(f"Failed to get dataset instance: {response.error}")

        logger.info("Successfully retrieved dataset instance")
        return response.result

    async def get_quota(
        self,
        ds: str,
        quota_type: Optional[
            Literal["USER", "GROUP", "DATASET", "PROJECT"]
        ] = "DATASET",
        relationships: bool = True,
        extend: Optional[str] = None,
        extend_context: Optional[str] = None,
        prefix: Optional[str] = None,
        extra: Dict = None,
        order_by: list = None,
        select: list = None,
        count: bool = False,
        get: bool = False,
        offset: int = 0,
        limit: int = 0,
        force_sql_filters: bool = True,
    ) -> list:
        """Get a list of `quota_type` quotas for dataset `ds`. This method
        assumes quota_type "DATASET" if none is provided.

        When quota_type is not DATASET, each quota entry has these fields:
            id          - the uid or gid to which the quota applies.
            name        - the user or group name to which the quota applies.
                          Value is null if the id in the quota cannot be
                          resolved to a user or group. This indicates that
                          the user or group does not exist on the server.
            quota       - the quota size in bytes. Absent if no quota is set.
            used_bytes  - the amount of bytes the user has written to the
                          dataset. A value of zero means unlimited.
            obj_quota   - the number of objects that may be owned by id.
                          A value of zero means unlimited. Absent if no
                          objquota is set.
            obj_used    - the number of objects currently owned by id.

        Returns:
            List of quotas

        Raises:
            DatasetError: If dataset is not found or other error occurs
        """
        logger.debug("Getting quotas of type %s for dataset %s", quota_type, ds)

        # Build options dict with non-None values
        options = {
            "relationships": relationships,
            "extend": extend,
            "extend_context": extend_context,
            "prefix": prefix,
            "extra": extra or {},
            "order_by": order_by or [],
            "select": select or [],
            "count": count,
            "get": get,
            "offset": offset,
            "limit": limit,
            "force_sql_filters": force_sql_filters,
        }

        # Remove None values
        options = {k: v for k, v in options.items() if v is not None}

        response = await self.conn._call(
            "pool.dataset.get_quota", [ds, quota_type, options]
        )
        if response.error:
            logger.error("Failed to retrieve quotas for dataset: %s", response.error)
            raise DatasetError(f"Failed to get dataset quotas: {response.error}")

        logger.info("Successfully retrieved dataset quotas")
        return response.result

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

        logger.debug("Calling pool.dataset.query with params %s", params)
        response = await self.conn._call("pool.dataset.query", params)
        if response.error:
            logger.error("Failed to query datasets: %s", response.error)
            raise DatasetError(f"Failed to query datasets: {response.error}")

        logger.info("Successfully queried datasets")
        return response.result


class DatasetError(Exception):
    """Raised when a dataset operation fails."""

    pass
