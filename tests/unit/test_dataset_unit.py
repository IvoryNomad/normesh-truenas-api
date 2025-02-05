# test_dataset.py
import pytest
from unittest.mock import AsyncMock, patch
from truenas_api.dataset import DatasetManager, DatasetError
from truenas_api.connection import TrueNASResponse


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
async def test_dataset_create():
    """Test dataset creation."""
    conn = AsyncMock()
    conn._call.return_value = TrueNASResponse(
        id="1", result={"id": "tank/newdataset", "type": "FILESYSTEM"}, error=None
    )

    manager = DatasetManager(conn)
    result = await manager.create("tank/newdataset", properties={"compression": "lz4"})

    assert result["id"] == "tank/newdataset"

    # Verify correct API call
    conn._call.assert_called_once_with(
        "pool.dataset.create",
        [
            {
                "name": "tank/newdataset",
                "type": "FILESYSTEM",
                "properties": {"compression": "lz4"},
            }
        ],
    )
