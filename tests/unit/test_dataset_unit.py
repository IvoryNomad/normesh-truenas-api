from unittest.mock import AsyncMock, patch

import pytest

from truenas_api.connection import TrueNASResponse
from truenas_api.dataset import DatasetError, DatasetManager


@pytest.mark.asyncio
async def test_create_basic_filesystem():
    """Test creating a basic filesystem with minimal parameters."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/testfs", "type": "FILESYSTEM"}, error=None
    )

    manager = DatasetManager(conn)
    result = await manager.create({"name": "tank/testfs", "type": "FILESYSTEM"})

    # Verify minimal params for filesystem
    conn._call.assert_called_once_with(
        "pool.dataset.create",
        [
            {
                "name": "tank/testfs",
                "type": "FILESYSTEM",
                "share_type": "GENERIC",
                "encryption": False,
                "inherit_encryption": True,
                "user_properties": [],
                "create_ancestors": False,
            }
        ],
    )


@pytest.mark.asyncio
async def test_create_volume_minimal():
    """Test creating a volume with only required parameters."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/testvol", "type": "VOLUME"}, error=None
    )

    manager = DatasetManager(conn)
    result = await manager.create(
        {"name": "tank/testvol", "type": "VOLUME", "volsize": 1024 * 1024 * 1024}  # 1GB
    )

    conn._call.assert_called_once_with(
        "pool.dataset.create",
        [
            {
                "name": "tank/testvol",
                "type": "VOLUME",
                "volsize": 1024 * 1024 * 1024,
                "share_type": "GENERIC",
                "encryption": False,
                "inherit_encryption": True,
                "user_properties": [],
                "create_ancestors": False,
            }
        ],
    )


# @pytest.mark.asyncio
# async def test_create_with_invalid_property():
#     """Test that invalid properties raise validation errors."""
#     conn = AsyncMock()
#     manager = DatasetManager(conn)
#
#     # Test invalid compression type
#     with pytest.raises(ValueError, match="Invalid compression type"):
#         await manager.create(
#             {
#                 "name": "tank/test",
#                 "compression": "INVALID",  # Type checker should catch this!
#             }
#         )
#
#     # Test invalid acltype for VOLUME
#     with pytest.raises(ValueError, match="acltype cannot be set on VOLUME"):
#         await manager.create(
#             {
#                 "name": "tank/test",
#                 "type": "VOLUME",
#                 "volsize": 1024 * 1024 * 1024,
#                 "acltype": "NFSV4",
#             }
#         )
#
#     # Test volume without size
#     with pytest.raises(ValueError, match="volsize required for VOLUME type"):
#         await manager.create({"name": "tank/test", "type": "VOLUME"})
#
#     # Test invalid encryption options
#     with pytest.raises(ValueError, match="passphrase or key required"):
#         await manager.create(
#             {
#                 "name": "tank/test",
#                 "encryption": True,
#                 "encryption_options": {
#                     "algorithm": "AES-256-GCM",
#                     "generate_key": False,
#                 },
#             }
#         )
#
#     # Verify no API calls were made
#     conn._call.assert_not_called()


@pytest.mark.asyncio
async def test_create_volume_with_blocksize():
    """Test creating a volume with block size specification."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/testvol", "type": "VOLUME"}, error=None
    )

    manager = DatasetManager(conn)
    result = await manager.create(
        properties={
            "name": "tank/testvol",
            "type": "VOLUME",
            "volsize": 1024 * 1024 * 1024,
            "volblocksize": "4K",
            "sparse": True,
        },
    )

    # Verify volume params with blocksize
    conn._call.assert_called_once_with(
        "pool.dataset.create",
        [
            {
                "name": "tank/testvol",
                "type": "VOLUME",
                "volsize": 1024 * 1024 * 1024,
                "volblocksize": "4K",
                "sparse": True,
                "share_type": "GENERIC",
                "encryption": False,
                "inherit_encryption": True,
                "user_properties": [],
                "create_ancestors": False,
            }
        ],
    )


@pytest.mark.asyncio
async def test_create_encrypted_dataset():
    """Test creating an encrypted dataset."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/secure", "type": "FILESYSTEM"}, error=None
    )

    manager = DatasetManager(conn)
    result = await manager.create(
        {
            "name": "tank/secure",
            "encryption": True,
            "encryption_options": {"generate_key": True, "algorithm": "AES-256-GCM"},
        }
    )

    # Verify encryption params
    conn._call.assert_called_once_with(
        "pool.dataset.create",
        [
            {
                "name": "tank/secure",
                "type": "FILESYSTEM",
                "encryption": True,
                #               "inherit_encryption": True,
                "encryption_options": {
                    "generate_key": True,
                    "algorithm": "AES-256-GCM",
                    "pbkdf2iters": 350000,
                    "passphrase": None,
                    "key": None,
                },
                "share_type": "GENERIC",
                "inherit_encryption": True,
                "user_properties": [],
                "create_ancestors": False,
            }
        ],
    )


@pytest.mark.asyncio
async def test_create_with_properties():
    """Test creating dataset with various ZFS properties."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/data", "type": "FILESYSTEM"}, error=None
    )

    manager = DatasetManager(conn)
    result = await manager.create(
        properties={
            "name": "tank/data",
            "compression": "LZ4",
            "atime": "OFF",
            "sync": "DISABLED",
            "quota": 5 * 1024 * 1024 * 1024,  # 5GB
            "recordsize": "128K",
            "acltype": "NFSV4",
        },
    )

    # Verify property setting
    conn._call.assert_called_once_with(
        "pool.dataset.create",
        [
            {
                "name": "tank/data",
                "type": "FILESYSTEM",
                "compression": "LZ4",
                "atime": "OFF",
                "sync": "DISABLED",
                "quota": 5 * 1024 * 1024 * 1024,
                "recordsize": "128K",
                "acltype": "NFSV4",
                "share_type": "GENERIC",
                "encryption": False,
                "inherit_encryption": True,
                "user_properties": [],
                "create_ancestors": False,
            }
        ],
    )


@pytest.mark.asyncio
async def test_create_with_ancestors():
    """Test creating dataset with ancestor creation enabled."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/parent/child", "type": "FILESYSTEM"}, error=None
    )

    manager = DatasetManager(conn)
    result = await manager.create(
        {"name": "tank/parent/child", "create_ancestors": True}
    )

    # Verify ancestor creation flag
    conn._call.assert_called_once_with(
        "pool.dataset.create",
        [
            {
                "name": "tank/parent/child",
                "type": "FILESYSTEM",
                "create_ancestors": True,
                "share_type": "GENERIC",
                "encryption": False,
                "inherit_encryption": True,
                "user_properties": [],
            }
        ],
    )


@pytest.mark.asyncio
async def test_create_smb_share():
    """Test creating dataset configured for SMB sharing."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/share", "type": "FILESYSTEM"}, error=None
    )

    manager = DatasetManager(conn)
    result = await manager.create(
        {
            "name": "tank/share",
            "share_type": "SMB",
            "aclmode": "RESTRICTED",
            "acltype": "NFSV4",
        },
    )

    # Verify SMB share configuration
    conn._call.assert_called_once_with(
        "pool.dataset.create",
        [
            {
                "name": "tank/share",
                "type": "FILESYSTEM",
                "share_type": "SMB",
                "aclmode": "RESTRICTED",
                "acltype": "NFSV4",
                "encryption": False,
                "inherit_encryption": True,
                "user_properties": [],
                "create_ancestors": False,
            }
        ],
    )


# Error test cases
@pytest.mark.asyncio
async def test_create_volume_missing_size():
    """Test that creating a volume without size fails."""
    conn = AsyncMock()
    manager = DatasetManager(conn)

    with pytest.raises(DatasetError, match="volsize required for VOLUME type"):
        await manager.create({"name": "tank/testvol", "type": "VOLUME"})

    # Verify no API call was made
    conn._call.assert_not_called()


@pytest.mark.asyncio
async def test_create_volume_invalid_blocksize():
    """Test that invalid blocksize is caught."""
    conn = AsyncMock()
    manager = DatasetManager(conn)

    with pytest.raises(DatasetError, match="Invalid volblocksize"):
        await manager.create(
            {
                "name": "tank/testvol",
                "type": "VOLUME",
                "volsize": 1024 * 1024 * 1024,
                "volblocksize": "3K",  # Invalid size
            },
        )

    # Verify no API call was made
    conn._call.assert_not_called()


@pytest.mark.asyncio
async def test_create_api_error():
    """Test handling of API errors during creation."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result=None, error="Dataset already exists"
    )

    manager = DatasetManager(conn)

    with pytest.raises(
        DatasetError, match="Failed to create dataset: Dataset already exists"
    ):
        await manager.create({"name": "tank/exists"})


@pytest.mark.asyncio
async def test_get_instance_basic():
    """Test getting a dataset instance with defaults."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/testfs", "type": "FILESYSTEM"}, error=None
    )

    manager = DatasetManager(conn)
    result = await manager.get_instance("tank/testfs")

    # Verify API call
    conn._call.assert_called_once_with(
        "pool.dataset.get_instance",
        [
            "tank/testfs",
            {
                "relationships": True,
                "extra": {},
                "order_by": [],
                "select": [],
                "count": False,
                "get": False,
                "offset": 0,
                "limit": 0,
                "force_sql_filters": True,
            },
        ],
    )


@pytest.mark.asyncio
async def test_get_instance_with_options():
    """Test getting a dataset instance with custom options."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/testfs", "type": "FILESYSTEM"}, error=None
    )

    manager = DatasetManager(conn)
    result = await manager.get_instance(
        "tank/testfs",
        relationships=False,
        extend="pool",
        select=["name", "type"],
        limit=1,
    )

    # Verify API call
    conn._call.assert_called_once_with(
        "pool.dataset.get_instance",
        [
            "tank/testfs",
            {
                "relationships": False,
                "extend": "pool",
                "extra": {},
                "order_by": [],
                "select": ["name", "type"],
                "count": False,
                "get": False,
                "offset": 0,
                "limit": 1,
                "force_sql_filters": True,
            },
        ],
    )


@pytest.mark.asyncio
async def test_get_instance_not_found():
    """Test handling of non-existent dataset."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result=None, error="Dataset not found"
    )

    manager = DatasetManager(conn)
    with pytest.raises(
        DatasetError, match="Failed to get dataset instance: Dataset not found"
    ):
        await manager.get_instance("tank/nonexistent")


@pytest.mark.asyncio
async def test_get_instance_boolean_id():
    """Test that boolean ids raise NotImplementedError."""
    conn = AsyncMock()
    manager = DatasetManager(conn)

    with pytest.raises(
        NotImplementedError,
        match="Boolean values for dataset id are not currently supported",
    ):
        await manager.get_instance(True)

    # Verify no API call was made
    conn._call.assert_not_called()


@pytest.mark.asyncio
async def test_get_quota_default_type():
    """Test getting quotas with default quota_type (DATASET)."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result=[{"quota": 1024 * 1024 * 1024}], error=None  # 1GB quota
    )

    manager = DatasetManager(conn)
    result = await manager.get_quota("tank/testds")

    # Verify API call uses default DATASET type
    conn._call.assert_called_once_with(
        "pool.dataset.get_quota",
        [
            "tank/testds",
            "DATASET",
            {
                "relationships": True,
                "extra": {},
                "order_by": [],
                "select": [],
                "count": False,
                "get": False,
                "offset": 0,
                "limit": 0,
                "force_sql_filters": True,
            },
        ],
    )


@pytest.mark.asyncio
async def test_get_quota_user_type():
    """Test getting USER quotas with expected return fields."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1",
        result=[
            {
                "id": 1000,
                "name": "testuser",
                "quota": 1024 * 1024 * 1024,
                "used_bytes": 500 * 1024 * 1024,
                "obj_quota": 1000,
                "obj_used": 50,
            }
        ],
        error=None,
    )

    manager = DatasetManager(conn)
    result = await manager.get_quota("tank/testds", quota_type="USER")

    # Verify call with USER type
    conn._call.assert_called_once_with(
        "pool.dataset.get_quota",
        [
            "tank/testds",
            "USER",
            {
                "relationships": True,
                "extra": {},
                "order_by": [],
                "select": [],
                "count": False,
                "get": False,
                "offset": 0,
                "limit": 0,
                "force_sql_filters": True,
            },
        ],
    )

    # Verify returned quota structure
    assert len(result) == 1
    quota = result[0]
    assert quota["id"] == 1000
    assert quota["name"] == "testuser"
    assert quota["quota"] == 1024 * 1024 * 1024
    assert quota["used_bytes"] == 500 * 1024 * 1024
    assert quota["obj_quota"] == 1000
    assert quota["obj_used"] == 50


@pytest.mark.asyncio
async def test_get_quota_with_options():
    """Test getting quotas with custom query options."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result=[{"quota": 1024 * 1024 * 1024}], error=None
    )

    manager = DatasetManager(conn)
    result = await manager.get_quota(
        "tank/testds", quota_type="GROUP", select=["name", "quota"], limit=10
    )

    # Verify options are passed correctly
    conn._call.assert_called_once_with(
        "pool.dataset.get_quota",
        [
            "tank/testds",
            "GROUP",
            {
                "relationships": True,
                "extra": {},
                "order_by": [],
                "select": ["name", "quota"],
                "count": False,
                "get": False,
                "offset": 0,
                "limit": 10,
                "force_sql_filters": True,
            },
        ],
    )


@pytest.mark.asyncio
async def test_get_quota_api_error():
    """Test handling of API errors."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result=None, error="Dataset not found"
    )

    manager = DatasetManager(conn)
    with pytest.raises(
        DatasetError, match="Failed to get dataset quotas: Dataset not found"
    ):
        await manager.get_quota("tank/nonexistent")


@pytest.mark.asyncio
async def test_dataset_query():
    """Test basic dataset query."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1",
        result=[
            {"id": "tank/test", "type": "FILESYSTEM"},
            {"id": "tank/test2", "type": "FILESYSTEM"},
        ],
        error=None,
    )

    manager = DatasetManager(conn)
    result = await manager.query()

    assert len(result) == 2
    assert result[0]["id"] == "tank/test"

    # Verify correct API call
    conn._call.assert_called_once_with("pool.dataset.query", [])


@pytest.mark.asyncio
async def test_set_quota():
    """Test setting dataset quotas."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(id="1", result=None, error=None)

    manager = DatasetManager(conn)

    # Test setting a dataset quota
    await manager.set_quota(
        "tank/testds",
        [
            {
                "quota_type": "DATASET",
                "id": "0",
                "quota_value": 10 * 1024 * 1024 * 1024,  # 10GB
            }
        ],
    )

    # Verify API call
    conn._call.assert_called_once_with(
        "pool.dataset.set_quota",
        [
            "tank/testds",
            [{"quota_type": "DATASET", "id": "0", "quota_value": 10737418240}],
        ],
    )

    # Reset mock for next test
    conn._call.reset_mock()

    # Test setting multiple quotas
    await manager.set_quota(
        "tank/testds",
        [
            {
                "quota_type": "USER",
                "id": "1000",
                "quota_value": 5 * 1024 * 1024 * 1024,  # 5GB
            },
            {"quota_type": "GROUP", "id": "100", "quota_value": None},  # Remove quota
        ],
    )

    # Verify API call
    conn._call.assert_called_once_with(
        "pool.dataset.set_quota",
        [
            "tank/testds",
            [
                {"quota_type": "USER", "id": "1000", "quota_value": 5368709120},
                {"quota_type": "GROUP", "id": "100", "quota_value": None},
            ],
        ],
    )


@pytest.mark.asyncio
async def test_set_quota_error():
    """Test error handling when setting quotas."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result=None, error="Dataset not found"
    )

    manager = DatasetManager(conn)

    with pytest.raises(DatasetError, match="Failed to set quotas: Dataset not found"):
        await manager.set_quota(
            "tank/nonexistent",
            [{"quota_type": "DATASET", "id": "0", "quota_value": 1024 * 1024 * 1024}],
        )


@pytest.mark.asyncio
async def test_set_quota_none():
    """Test setting quotas with None argument."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(id="1", result=None, error=None)

    manager = DatasetManager(conn)

    # Verify that None is converted to empty list
    await manager.set_quota("tank/testds", None)

    conn._call.assert_called_once_with(
        "pool.dataset.set_quota", ["tank/testds", []]  # Should pass empty list
    )


@pytest.mark.asyncio
async def test_update_basic_properties():
    """Test updating basic dataset properties."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/testds", "type": "FILESYSTEM"}, error=None
    )

    manager = DatasetManager(conn)

    # Test updating multiple properties
    await manager.update(
        "tank/testds",
        {"compression": "LZ4", "atime": "OFF", "quota": 5 * 1024 * 1024 * 1024},  # 5GB
    )

    # Verify API call
    conn._call.assert_called_once_with(
        "pool.dataset.update",
        ["tank/testds", {"compression": "LZ4", "atime": "OFF", "quota": 5368709120}],
    )


@pytest.mark.asyncio
async def test_update_with_inheritance():
    """Test setting properties to inherit from parent."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/testds", "type": "FILESYSTEM"}, error=None
    )

    manager = DatasetManager(conn)

    await manager.update(
        "tank/testds",
        {"compression": "INHERIT", "atime": "INHERIT", "recordsize": "INHERIT"},
    )

    # Verify API call
    conn._call.assert_called_once_with(
        "pool.dataset.update",
        [
            "tank/testds",
            {"compression": "INHERIT", "atime": "INHERIT", "recordsize": "INHERIT"},
        ],
    )


@pytest.mark.asyncio
async def test_update_user_properties():
    """Test updating user properties."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/testds", "type": "FILESYSTEM"}, error=None
    )

    manager = DatasetManager(conn)

    # Test adding and removing user properties
    await manager.update(
        "tank/testds",
        {
            "user_properties_update": [
                {"key": "custom:owner", "value": "department1"},
                {"key": "custom:temporary", "remove": True},
            ]
        },
    )

    # Verify API call
    conn._call.assert_called_once_with(
        "pool.dataset.update",
        [
            "tank/testds",
            {
                "user_properties_update": [
                    {"key": "custom:owner", "value": "department1"},
                    {"key": "custom:temporary", "remove": True},
                ]
            },
        ],
    )


@pytest.mark.asyncio
async def test_update_error():
    """Test error handling during update."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result=None, error="Dataset not found"
    )

    manager = DatasetManager(conn)

    with pytest.raises(
        DatasetError, match="Failed to update dataset: Dataset not found"
    ):
        await manager.update("tank/nonexistent", {"compression": "LZ4"})
