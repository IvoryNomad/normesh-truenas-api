import logging

import pytest


@pytest.fixture
def debug_logging():
    """Enable debug logging for tests using this fixture."""
    # Store original levels to restore later
    original_levels = {
        "root": logging.getLogger().getEffectiveLevel(),
        "truenas_api": logging.getLogger("truenas_api").getEffectiveLevel(),
    }

    # configure the root logger
    logging.getLogger().setLevel(logging.DEBUG)

    # configure the module logger
    logger = logging.getLogger("truenas_api")
    logger.setLevel(logging.DEBUG)

    # ensure we have a handler that will display the logs
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        logger.addHandler(handler)

    # The yield statement separates setup from cleanup
    yield

    # Restore original logging levels
    logging.getLogger().setLevel(original_levels["root"])
    logger.setLevel(original_levels["truenas_api"])
