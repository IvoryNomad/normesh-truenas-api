import json
import os

import pytest
from pytest_asyncio import fixture

from truenas_api.connection import TrueNASConnection
from truenas_api.dataset import DatasetManager


@fixture(scope="function")
async def truenas_connection():
    """Create a TrueNAS connection for integration testing."""
    host = os.getenv("TRUENAS_HOST")
    username = os.getenv("TRUENAS_USERNAME")
    password = os.getenv("TRUENAS_PASSWORD")

    if not all([host, username, password]):
        pytest.skip("Missing required environment variables for integration testing")

    conn = TrueNASConnection(host, username, password)
    await conn.connect()

    yield conn

    await conn.disconnect()

@fixture(scope="function")
async def dataset_manager(truenas_connection):
    """Create a DatasetManager instance for testing."""
    return DatasetManager(truenas_connection)

@pytest.mark.integration
@pytest.mark.asyncio
async def test_dataset_query(dataset_manager):
    """Test querying datasets from a live TrueNAS system.

    This test verifies that:
    1. We can successfully query datasets
    2. The response has the expected structure
    3. Basic dataset properties are present
    """
    # Query all datasets
    datasets = await dataset_manager.query()

    print("\nDataset Query Results:")
    for dataset in datasets:
        print(f"\nDataset: {dataset['name']}")
        print(f"Type: {dataset['type']}")
        print(f"Properties: {json.dumps(dataset.get('properties', {}), indent=2)}")

    # Verify we got a list of datasets
    assert isinstance(datasets, list)
    assert len(datasets) > 0  # We expect at least one dataset to exist

    # Check structure of first dataset
    first_dataset = datasets[0]
    # Required fields that should always be present
    assert "id" in first_dataset
    assert "type" in first_dataset
    assert "name" in first_dataset

    # Try querying with a filter for a specific dataset
    filtered = await dataset_manager.query(
        filters=[["id", "=", first_dataset["id"]]]
    )
    assert len(filtered) == 1
    assert filtered[0]["id"] == first_dataset["id"]
