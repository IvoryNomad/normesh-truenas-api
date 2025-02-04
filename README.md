# Normesh TrueNAS API

A community-developed Python library for interacting with the TrueNAS WebSocket API. This library provides a clean, intuitive interface for automating TrueNAS operations and serves as the foundation for the normesh-truenas Ansible collection.

*Note: This is a community project and is not affiliated with or endorsed by iXsystems or TrueNAS.*

## Overview

Managing TrueNAS systems often requires automation, whether for maintaining datasets, configuring shares, or managing system settings. While TrueNAS provides a WebSocket API, working with it directly can be complex. This library abstracts away that complexity, providing a Pythonic interface that makes automation straightforward and reliable.

This library was created to support the normesh-truenas Ansible collection but is designed to be useful in any Python project that needs to interact with TrueNAS systems. By separating the core API interaction logic into its own package, we ensure that the code is well-tested, maintainable, and reusable across different automation tools.

## Features

Currently in development, with planned support for:

- Secure WebSocket connection management
- Dataset operations (creation, deletion, property management)
- Share configuration (SMB, NFS)
- Device operations (certificates, cloud backup, configuration)
- Comprehensive error handling and validation

## Installation

Once released, the package will be available on PyPI:

```bash
pip install truenas-api
```

## Quick Start

Here's a simple example of using the library to connect to a TrueNAS system and create a dataset:

```python
import asyncio
from truenas_api import TrueNASConnection

async def main():
    # Initialize connection
    truenas = TrueNASConnection(
        host="truenas.local",
        api_key="your-api-key"
    )
    
    # Connect to TrueNAS
    await truenas.connect()
    
    try:
        # Create a dataset
        dataset_manager = DatasetManager(truenas)
        await dataset_manager.create_dataset(
            name="tank/my_dataset",
            properties={
                "compression": "lz4",
                "atime": "off"
            }
        )
    finally:
        # Always clean up connection
        await truenas.disconnect()

# Run the async function
asyncio.run(main())
```

## Development

This project is under active development. To contribute:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/truenas-api.git
   cd truenas-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```

3. Install development dependencies:
   ```bash
   pip install -e ".[test]"
   ```

4. Run tests:
   ```bash
   pytest
   ```

### Testing with Live TrueNAS System

The test suite includes both mock tests and integration tests. To run integration tests against a live TrueNAS system:

1. Set up environment variables:
   ```bash
   export TRUENAS_HOST="your-truenas-host"
   export TRUENAS_API_KEY="your-api-key"
   ```

2. Run integration tests:
   ```bash
   pytest --runintegration
   ```

## Related Projects

- normesh-truenas Ansible Collection: Ansible collection that uses this library to provide TrueNAS automation capabilities within Ansible.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate and follow the existing code style.

## Project Status

This project is in active development on the `dev` branch. The initial focus is on establishing core functionality and comprehensive testing. Production releases will be tagged and merged to the `master` branch once they are stable and well-tested.