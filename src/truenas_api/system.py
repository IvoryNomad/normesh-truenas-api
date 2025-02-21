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


class DiskManager:
    """Manages disk operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    disk.details                                        |     No      |         | No
    disk.get_instance                                   |     No      |         | No
    disk.get_unused                                     |     No      |         | No
    disk.get_used                                       |     No      |         | No
    disk.query                                          |     No      |         | No
    disk.resize                                         |     No      |         | Yes
    disk.retaste                                        |     No      |         | Yes
    disk.smart_attributes                               |     No      |         | No
    disk.temperature                                    |     No      |         | No
    disk.temperature_agg                                |     No      |         | No
    disk.temperature_alerts                             |     No      |         | No
    disk.temperatures                                   |     No      |         | No
    disk.update                                         |     No      |         | No
    disk.wipe                                           |     No      |         | Yes
    disk.                                               |     No      |         | No
    disk.                                               |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize system disk manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class EnclosureManager:
    """Manages system enclosure operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    enclosure.get_instance                              |     No      |         | No
    enclosure.query                                     |     No      |         | No
    enclosure.set_slot_status                           |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize system enclosure manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class FailoverManager:
    """Manages system failover operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    failover.become_passive                             |     No      |         | No
    failover.call_remote                                |     No      |         | No
    failover.config                                     |     No      |         | No
    failover.control                                    |     No      |         | No
    failover.force_master                               |     No      |         | No
    failover.get_ips                                    |     No      |         | No
    failover.hardware                                   |     No      |         | No
    failover.in_progress                                |     No      |         | No
    failover.licensed                                   |     No      |         | No
    failover.node                                       |     No      |         | No
    failover.status                                     |     No      |         | No
    failover.sync_from_peer                             |     No      |         | No
    failover.sync_to_peer                               |     No      |         | No
    failover.unlock                                     |     No      |         | No
    failover.update                                     |     No      |         | No
    failover.upgrade                                    |     No      |         | Yes
    failover.upgrade_finish                             |     No      |         | Yes
    failover.upgrade_pending                            |     No      |         | No
    failover.disabled.reasons                           |     No      |         | No
    failover.reboot.info                                |     No      |         | No
    failover.reboot.reboot_other_node                   |     No      |         | Yes
    failover.reboot.reboot_required                     |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize system failover manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...
