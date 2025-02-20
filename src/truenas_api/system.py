import logging
from typing import Any, Dict, Optional

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class BootManager:
    """Manages system boot operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    boot.attach                                         |     No      |         | Yes
    boot.detach                                         |     No      |         | No
    boot.get_disks                                      |     No      |         | No
    boot.get_scrub_interval                             |     No      |         | No
    boot.get_state                                      |     No      |         | No
    boot.replace                                        |     No      |         | Yes
    boot.scrub                                          |     No      |         | Yes
    boot.set_scrub_interval                             |     No      |         | No
    bootenv.activate                                    |     No      |         | No
    bootenv.create                                      |     No      |         | No
    bootenv.delete                                      |     No      |         | Yes
    bootenv.get_instance                                |     No      |         | No
    bootenv.query                                       |     No      |         | No
    bootenv.set_attribute                               |     No      |         | No
    bootenv.update                                      |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize boot manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class ConfigManager:
    """Manages system configuration operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    config.reset                                        |     No      |         | Yes
    config.save                                         |     No      |         | Yes
    config.upload                                       |     No      |         | Yes

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize system config manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class CronJobManager:
    """Manages system cron job operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    cronjob.create                                      |     No      |         | No
    cronjob.delete                                      |     No      |         | No
    cronjob.get_instance                                |     No      |         | No
    cronjob.query                                       |     No      |         | No
    cronjob.run                                         |     No      |         | Yes
    cronjob.update                                      |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize system cron job manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class DeviceManager:
    """Manages system device operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    device.get_info                                     |     No      |         | No
    device.gpu_pci_ids_choices                          |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize system device manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...
