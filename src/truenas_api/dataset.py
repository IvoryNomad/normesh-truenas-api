import logging
from typing import Any, Dict, List, Literal, Optional, TypedDict, Union

from .connection import TrueNASConnection, TrueNASResponse

# Create module logger
logger = logging.getLogger(__name__)


class QuotaEntry(TypedDict):
    """Type definition for a single quota entry.

    Attributes:
        quota_type: Type of quota
        id: Identifier for quota (e.g. user id, group id)_
        quota_value: Size of quota in bytes, or None to remove quota
    """

    quota_type: Literal["DATASET", "USER", "USEROBJ", "GROUP", "GROUPOBJ"]
    id: str
    quota_value: Optional[int]


class UserProperty(TypedDict):
    """Type definition for a user property.

    Attributes:
        key: Name of the property
        value: Value for the property
    """

    key: str
    value: str


class EncryptionOptions(TypedDict, total=False):
    """Type definition for dataset encryption options.

    All fields are optional with defaults provided by the API.

    Attributes:
        generate_key: Whether to auto-generate an encryption key
        pbkdf2iters: Number of PBKDF2 iterations for passphrase
        algorithm: Encryption algorithm to use
        passphrase: Encryption passphrase (required if using passphrase)
        key: Hex-encoded key (required if not using passphrase or generate_key)
    """

    generate_key: bool  # default: False
    pbkdf2iters: int  # default: 350000
    algorithm: Literal[
        "AES-128-CCM",
        "AES-192-CCM",
        "AES-256-CCM",
        "AES-128-GCM",
        "AES-192-GCM",
        "AES-256-GCM",
    ]  # default: "AES-256-GCM"
    passphrase: Optional[str]  # default: None
    key: Optional[str]  # default: None


# class ZFSCreateProperties(TypedDict, total=False):
#     """Type definition for ZFS dataset creation properties.
#
#     This class defines all properties that can be set when creating a new dataset.
#     Using total=False since all properties except 'name' are optional.
#     Many properties can be set to "INHERIT" to inherit from parent.
#
#     Attributes:
#         name: Full name of dataset (e.g. "tank/mydataset")
#         type: Type of dataset to create
#         volsize: Size in bytes (required for VOLUME type)
#         volblocksize: Block size for VOLUME type
#         sparse: Whether volume should be sparse (thin provisioned)
#         force_size: Force the volume size, even if it may break things
#         comments: Dataset comments or description
#         sync: Sync behavior (STANDARD/ALWAYS/DISABLED)
#         compression: Compression algorithm to use
#         atime: Update access time on read (ON/OFF)
#         exec: Allow executable files (ON/OFF)
#         quota: Space quota in bytes
#         reservation: Space reservation in bytes
#         recordsize: Record size for filesystems
#         readonly: Read-only status (ON/OFF)
#         snapdir: .zfs directory visibility
#         deduplication: Deduplication status
#         aclmode: ACL processing mode
#         acltype: ACL implementation type
#         share_type: Sharing protocol configuration
#         encryption: Enable dataset encryption
#         encryption_options: Encryption settings
#         inherit_encryption: Inherit encryption from parent
#         user_properties: List of custom properties
#         create_ancestors: Create parent datasets if needed
#     """
#
#     name: str  # This is the only required field
#     type: Literal["FILESYSTEM", "VOLUME"]  # default: "FILESYSTEM"
#     volsize: Optional[int]  # Required for VOLUME type
#     volblocksize: Literal[
#         "512", "512B", "1K", "2K", "4K", "8K", "16K", "32K", "64K", "128K"
#     ]
#     sparse: bool
#     force_size: bool
#     comments: Union[str, Literal["INHERIT"]]
#     sync: Union[Literal["STANDARD", "ALWAYS", "DISABLED"], Literal["INHERIT"]]
#     snapdev: Union[Literal["HIDDEN", "VISIBLE"], Literal["INHERIT"]]
#     compression: Union[
#         Literal[
#             "ON",
#             "OFF",
#             "LZ4",
#             "GZIP",
#             "GZIP-1",
#             "GZIP-9",
#             "ZSTD",
#             "ZSTD-FAST",
#             "ZLE",
#             "LZJB",
#             "ZSTD-1",
#             "ZSTD-2",
#             "ZSTD-3",
#             "ZSTD-4",
#             "ZSTD-5",
#             "ZSTD-6",
#             "ZSTD-7",
#             "ZSTD-8",
#             "ZSTD-9",
#             "ZSTD-10",
#             "ZSTD-11",
#             "ZSTD-12",
#             "ZSTD-13",
#             "ZSTD-14",
#             "ZSTD-15",
#             "ZSTD-16",
#             "ZSTD-17",
#             "ZSTD-18",
#             "ZSTD-19",
#         ],
#         Literal["INHERIT"],
#     ]
#     atime: Union[Literal["ON", "OFF"], Literal["INHERIT"]]
#     exec: Union[Literal["ON", "OFF"], Literal["INHERIT"]]
#     managedby: Union[str, Literal["INHERIT"]]
#     quota: Optional[int]
#     quota_warning: Union[int, Literal["INHERIT"]]
#     quota_critical: Union[int, Literal["INHERIT"]]
#     refquota: Optional[int]
#     refquota_warning: Union[int, Literal["INHERIT"]]
#     refquota_critical: Union[int, Literal["INHERIT"]]
#     reservation: int
#     refreservation: int
#     special_small_block_size: Union[int, Literal["INHERIT"]]
#     copies: Union[int, Literal["INHERIT"]]
#     snapdir: Union[Literal["VISIBLE", "HIDDEN"], Literal["INHERIT"]]
#     deduplication: Union[Literal["ON", "VERIFY", "OFF"], Literal["INHERIT"]]
#     checksum: Union[
#         Literal[
#             "ON",
#             "OFF",
#             "FLETCHER2",
#             "FLETCHER4",
#             "SHA256",
#             "SHA512",
#             "SKEIN",
#             "EDONR",
#             "BLAKE3",
#         ],
#         Literal["INHERIT"],
#     ]
#     readonly: Union[Literal["ON", "OFF"], Literal["INHERIT"]]
#     recordsize: Union[str, Literal["INHERIT"]]
#     casesensitivity: Union[Literal["SENSITIVE", "INSENSITIVE"], Literal["INHERIT"]]
#     aclmode: Union[Literal["PASSTHROUGH", "RESTRICTED", "DISCARD"], Literal["INHERIT"]]
#     acltype: Union[Literal["OFF", "NFSV4", "POSIX"], Literal["INHERIT"]]
#     share_type: Literal["GENERIC", "MULTIPROTOCOL", "NFS", "SMB", "APPS"]
#     encryption_options: Optional[EncryptionOptions]
#     encryption: bool
#     inherit_encryption: bool
#     user_properties: List[UserProperty]
#     create_ancestors: bool


class ZFSCreateProperties(TypedDict, total=False):
    """Type definition for ZFS dataset creation properties.

    This class defines the complete set of properties that can be used when creating
    a new ZFS dataset through TrueNAS. While only 'name' is strictly required, many
    properties have system defaults that will be applied if not specified.

    Required Properties:
        name: Full name of dataset (e.g. "tank/mydataset")

    Common Optional Properties with Defaults:
        type: "FILESYSTEM" or "VOLUME" (default: "FILESYSTEM")
        encryption: Enable dataset encryption (default: False)
        inherit_encryption: Inherit parent encryption settings (default: True)
        create_ancestors: Create parent datasets if missing (default: False)
        share_type: Sharing protocol configuration (default: "GENERIC")

    Properties that Require Specific Dataset Types:
        volsize: Required for VOLUME type datasets (size in bytes)
        volblocksize: Block size for VOLUME type ("512" to "128K")
        sparse: Thin provisioning for VOLUME type (default: False)

    Inheritable Properties:
        These properties can be set to specific values or "INHERIT":
        compression: Data compression algorithm
        sync: Sync behavior for writes
        atime: Access time updates
        exec: Allow executable files
        snapdir: .zfs directory visibility
        readonly: Read-only status
        recordsize: Record size for filesystems

    Special Properties:
        encryption_options: Only used when encryption=True
        user_properties: Custom properties (key-value pairs)

    Note: Properties MUST appear in the order below as this is part of the API specification
    """

    name: str
    type: Literal["FILESYSTEM", "VOLUME"]
    volsize: Optional[int]
    volblocksize: Literal[
        "512", "512B", "1K", "2K", "4K", "8K", "16K", "32K", "64K", "128K"
    ]
    sparse: bool
    force_size: bool
    comments: Union[str, Literal["INHERIT"]]
    sync: Union[Literal["STANDARD", "ALWAYS", "DISABLED"], Literal["INHERIT"]]
    snapdev: Union[Literal["HIDDEN", "VISIBLE"], Literal["INHERIT"]]
    compression: Union[
        Literal["ON", "OFF", "LZ4", "GZIP", "GZIP-1", "GZIP-9", "ZSTD", ...],
        Literal["INHERIT"],
    ]
    atime: Union[Literal["ON", "OFF"], Literal["INHERIT"]]
    exec: Union[Literal["ON", "OFF"], Literal["INHERIT"]]
    managedby: Union[str, Literal["INHERIT"]]
    quota: Optional[int]
    quota_warning: Union[int, Literal["INHERIT"]]
    quota_critical: Union[int, Literal["INHERIT"]]
    refquota: Optional[int]
    refquota_warning: Union[int, Literal["INHERIT"]]
    refquota_critical: Union[int, Literal["INHERIT"]]
    reservation: int
    refreservation: int
    special_small_block_size: Union[int, Literal["INHERIT"]]
    copies: Union[int, Literal["INHERIT"]]
    snapdir: Union[Literal["VISIBLE", "HIDDEN"], Literal["INHERIT"]]
    deduplication: Union[Literal["ON", "VERIFY", "OFF"], Literal["INHERIT"]]
    checksum: Union[
        Literal[
            "ON",
            "OFF",
            "FLETCHER2",
            "FLETCHER4",
            "SHA256",
            "SHA512",
            "SKEIN",
            "EDONR",
            "BLAKE3",
        ],
        Literal["INHERIT"],
    ]
    readonly: Union[Literal["ON", "OFF"], Literal["INHERIT"]]
    recordsize: Union[str, Literal["INHERIT"]]
    casesensitivity: Union[Literal["SENSITIVE", "INSENSITIVE"], Literal["INHERIT"]]
    aclmode: Union[Literal["PASSTHROUGH", "RESTRICTED", "DISCARD"], Literal["INHERIT"]]
    acltype: Union[Literal["OFF", "NFSV4", "POSIX"], Literal["INHERIT"]]
    share_type: Literal["GENERIC", "MULTIPROTOCOL", "NFS", "SMB", "APPS"]
    encryption_options: Optional[EncryptionOptions]
    encryption: bool
    inherit_encryption: bool
    user_properties: List[UserProperty]
    create_ancestors: bool


class UserPropertyUpdate(TypedDict):
    """Type definition for updating a user property.

    Attributes:
        key: Name of the property to update
        value: New value for the property (optional if removing)
        remove: If True, remove this property
    """

    key: str
    value: Optional[str]
    remove: Optional[bool]


class ZFSUpdateProperties(TypedDict, total=False):
    """Type definition for updateable ZFS dataset properties.

    This class defines all properties that can be updated on an existing dataset.
    Using total=False since all properties are optional in updates.
    Many properties can be set to specific values or "INHERIT" to inherit from parent.

    Attributes:
        volsize: Size in bytes for VOLUME datasets
        force_size: Force the volume size, even if it may break things
        comments: Dataset comments or description
        sync: Sync behavior (STANDARD/ALWAYS/DISABLED)
        compression: Compression algorithm to use
        atime: Update access time on read (ON/OFF)
        exec: Allow executable files (ON/OFF)
        quota: Space quota in bytes
        reservation: Space reservation in bytes
        recordsize: Record size for filesystems
        readonly: Read-only status (ON/OFF)
        snapdir: .zfs directory visibility
        deduplication: Deduplication status
        aclmode: ACL processing mode
        acltype: ACL implementation type
        user_properties_update: List of user property updates
    """

    volsize: Optional[int]
    force_size: bool
    comments: Union[str, Literal["INHERIT"]]
    sync: Union[Literal["STANDARD", "ALWAYS", "DISABLED"], Literal["INHERIT"]]
    snapdev: Union[Literal["HIDDEN", "VISIBLE"], Literal["INHERIT"]]
    compression: Union[
        Literal[
            "ON",
            "OFF",
            "LZ4",
            "GZIP",
            "GZIP-1",
            "GZIP-9",
            "ZSTD",
            "ZSTD-FAST",
            "ZLE",
            "LZJB",
            "ZSTD-1",
            "ZSTD-2",
            "ZSTD-3",
            "ZSTD-4",
            "ZSTD-5",
            "ZSTD-6",
            "ZSTD-7",
            "ZSTD-8",
            "ZSTD-9",
            "ZSTD-10",
            "ZSTD-11",
            "ZSTD-12",
            "ZSTD-13",
            "ZSTD-14",
            "ZSTD-15",
            "ZSTD-16",
            "ZSTD-17",
            "ZSTD-18",
            "ZSTD-19",
        ],
        Literal["INHERIT"],
    ]
    atime: Union[Literal["ON", "OFF"], Literal["INHERIT"]]
    exec: Union[Literal["ON", "OFF"], Literal["INHERIT"]]
    managedby: Union[str, Literal["INHERIT"]]
    quota: Optional[int]
    quota_warning: Union[int, Literal["INHERIT"]]
    quota_critical: Union[int, Literal["INHERIT"]]
    refquota: Optional[int]
    refquota_warning: Union[int, Literal["INHERIT"]]
    refquota_critical: Union[int, Literal["INHERIT"]]
    reservation: int
    refreservation: int
    special_small_block_size: Union[int, Literal["INHERIT"]]
    copies: Union[int, Literal["INHERIT"]]
    snapdir: Union[Literal["VISIBLE", "HIDDEN"], Literal["INHERIT"]]
    deduplication: Union[Literal["ON", "VERIFY", "OFF"], Literal["INHERIT"]]
    checksum: Union[
        Literal[
            "ON",
            "OFF",
            "FLETCHER2",
            "FLETCHER4",
            "SHA256",
            "SHA512",
            "SKEIN",
            "EDONR",
            "BLAKE3",
        ],
        Literal["INHERIT"],
    ]
    readonly: Union[Literal["ON", "OFF"], Literal["INHERIT"]]
    recordsize: Union[str, Literal["INHERIT"]]
    aclmode: Union[Literal["PASSTHROUGH", "RESTRICTED", "DISCARD"], Literal["INHERIT"]]
    acltype: Union[Literal["OFF", "NFSV4", "POSIX"], Literal["INHERIT"]]
    user_properties_update: List[UserPropertyUpdate]


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
    pool.dataset.set_quota                              |     Yes     |  0.1.0  | No
    pool.dataset.snapshot_count                         |     No      |         | No
    pool.dataset.unlock                                 |     No      |         | Yes
    pool.dataset.unlock_services_restart_choices        |     No      |         | No
    pool.dataset.update                                 |     Yes     |  0.1.0  | No
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

    async def create(self, properties: ZFSCreateProperties) -> Dict:
        """Create a new dataset.

        This method creates a new ZFS dataset with the specified properties. All properties
        are passed in a single dictionary, with 'name' being the only required field.
        Other properties are optional and will use system defaults if not specified.

        Args:
            properties: Dictionary containing dataset properties. Valid keys include:
                name: Full name of dataset (e.g. "tank/dataset") - Required
                type: "FILESYSTEM" or "VOLUME" (default: "FILESYSTEM")
                volsize: Size in bytes (required for VOLUME type)
                compression: "ON", "OFF", "LZ4", "GZIP", etc., or "INHERIT"
                sync: "STANDARD", "ALWAYS", "DISABLED", or "INHERIT"
                atime: "ON", "OFF", or "INHERIT"
                quota: Space quota in bytes
                encryption: Enable dataset encryption (default: False)
                encryption_options: Dictionary with encryption settings:
                    generate_key: Whether to auto-generate a key
                    algorithm: "AES-256-GCM", etc.
                    passphrase: Encryption passphrase
                    key: Hex-encoded encryption key
                share_type: "GENERIC", "MULTIPROTOCOL", "NFS", "SMB", or "APPS"
                create_ancestors: Create parent datasets if needed (default: False)

                See ZFSCreateProperties type definition for complete list of
                valid properties and their allowed values.

        Returns:
            Dict: Information about the created dataset

        Raises:
            ValueError: If property validation fails (invalid values or combinations)
            DatasetError: If the API call fails

        Example:
            # Create basic filesystem
            await manager.create({"name": "tank/mydata"})

            # Create encrypted volume
            await manager.create({
                "name": "tank/secure",
                "type": "VOLUME",
                "volsize": 10 * 1024 * 1024 * 1024,  # 10GB
                "encryption": True,
                "encryption_options": {
                    "generate_key": True,
                    "algorithm": "AES-256-GCM"
                }
            })
        """

        # set defaults
        properties.setdefault("type", "FILESYSTEM")
        properties.setdefault("share_type", "GENERIC")
        properties.setdefault("encryption", False)
        properties.setdefault("inherit_encryption", True)
        properties.setdefault("user_properties", [])
        properties.setdefault("create_ancestors", False)

        # set encryption_options defaults when needed
        if properties.get("encryption"):
            properties.setdefault("encryption_options", {})
            enc_opts = properties["encryption_options"]
            enc_opts.setdefault("generate_key", False)
            enc_opts.setdefault("pbkdf2iters", 350000)
            enc_opts.setdefault("algorithm", "AES-256-GCM")
            enc_opts.setdefault("passphrase", None)  # Default is null in schema
            enc_opts.setdefault("key", None)  # Default is null in schema

        logger.debug(
            "Creating dataset %s of type %s", properties["name"], properties["type"]
        )

        # Validate VOLUME requirements
        if properties.get("type") == "VOLUME":
            if "volsize" not in properties:
                logger.error("Missing required volsize for VOLUME creation")
                raise DatasetError("volsize required for VOLUME type")
            if "volblocksize" in properties and properties["volblocksize"] not in (
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
            ):
                logger.error("Invalid volblocksize: %s", properties["volblocksize"])
                raise DatasetError("Invalid volblocksize")

        logger.debug("Calling pool.dataset.create with properties %s", properties)
        response = await self.conn._call("pool.dataset.create", [properties])
        if response.error:
            logger.error("Failed to create dataset: %s", response.error)
            raise DatasetError(f"Failed to create dataset: {response.error}")

        logger.info("Successfully created dataset %s", properties["name"])
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

    async def set_quota(
        self, ds: str, quotas: Optional[List[QuotaEntry]] = None
    ) -> None:
        """Set quotas omn a dataset.

        This method allows setting multiple quotas of different types on a dataset.
        If quota_value is None for an entry, that quota will be removed.

        Args:
            ds: Name of the dataset to set quotas on
            quotas: List of quota entries to apply. Each entry contains:
                   - quota_type: Type of quota ("DATASET", "USER", etc)
                   - id: ID for the quota (e.g. user/group id)
                   - quota_value: Size in bytes, or None to remove quota

        Raises:
            DatasetError: If quota setting fails

        Example:
            # Set a 10GB quota on a dataset
            await manager.set_quota("tank/data", [{
                "quota_type": "DATASET",
                "id": "0",
                "quota_value": 10 * 1024 * 1024 * 1024
            }])

            # Set a 5GB quota for user ID 1000
            await manager.set_quota("tank/home", [{
                "quota_type": "USER",
                "id": "1000",
                "quota_value": 5 * 1024 * 1024 * 1024
            }])
        """

        # Use default empty list if no quotas provided
        if quotas is None:
            quotas = []

        logger.debug("Setting quotas on dataset %s: %s", ds, quotas)
        response = await self.conn._call("pool.dataset.set_quota", [ds, quotas])
        if response.error:
            logger.error("Failed to set quotas: %s", response.error)
            raise DatasetError(f"Failed to set quotas: {response.error}")

        logger.info("Successfully set quotas on dataset %s", ds)

    async def update(self, id: str, properties: ZFSUpdateProperties) -> Dict:
        """Update properties of an existing dataset.

        This method allows updating properties on an existing dataset. Properties
        that aren't specified retain their current values. Many properties can
        be set to "INHERIT" to inherit from the parent dataset.

        Args:
            id: Name of dataset to update (e.g. "tank/dataset")
            properties: Dictionary of properties to update.
                       See ZFSUpdateProperties for valid options.

        Returns:
            Updated dataset information

        Raises:
            DatasetError: If update fails or properties are invalid

        Example:
            # Set compression and quota
            await manager.update("tank/data", {
                "compression": "LZ4",
                "quota": 5 * 1024 * 1024 * 1024  # 5GB
            })

            # Inherit properties from parent
            await manager.update("tank/data/sub", {
                "compression": "INHERIT",
                "recordsize": "INHERIT"
            })

            # Update a user property
            await manager.update("tank/data", {
                "user_properties_update": [{
                    "key": "custom:owner",
                    "value": "department1"
                }]
            })

            # Remove a user property
            await manager.update("tank/data", {
                "user_properties_update": [{
                    "key": "custom:temp",
                    "remove": True
                }]
            })
        """
        logger.debug("Updating dataset %s with properties: %s", id, properties)

        response = await self.conn._call("pool.dataset.update", [id, properties])
        if response.error:
            logger.error("Failed to update dataset: %s", response.error)
            raise DatasetError(f"Failed to update dataset: {response.error}")

        logger.info("Successfully updated dataset %s", id)
        return response.result


class DatasetError(Exception):
    """Raised when a dataset operation fails."""

    pass
