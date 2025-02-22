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


class HWManager:
    """Manages TrueNAS hardware operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    hardware.cpu.available_governors                    |     No      |         | No
    hardware.cpu.current_governor                       |     No      |         | No
    hardware.cpu.set_governor                           |     No      |         | No
    hardware.memory.error_info                          |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize hardware manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class InitShutdownScriptManager:
    """Manages TrueNAS initshutdownscript operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    initshutdownscript.create                           |     No      |         | No
    initshutdownscript.delete                           |     No      |         | No
    initshutdownscript.get_instance                     |     No      |         | No
    initshutdownscript.query                            |     No      |         | No
    initshutdownscript.update                           |     No      |         | No
    initshutdownscript.                                 |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize initshutdownscript manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class InterfaceManager:
    """Manages TrueNAS interface operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    interface.bridge_member_choices                     |     No      |         | No
    interface.cancel_rollback                           |     No      |         | No
    interface.checkin                                   |     No      |         | No
    interface.checkin_waiting                           |     No      |         | No
    interface.choices                                   |     No      |         | No
    interface.commit                                    |     No      |         | No
    interface.create                                    |     No      |         | No
    interface.default_route_will_be_removed             |     No      |         | No
    interface.delete                                    |     No      |         | No
    interface.get_instance                              |     No      |         | No
    interface.has_pending_changes                       |     No      |         | No
    interface.ip_in_use                                 |     No      |         | No
    interface.lacpdu_rate_choices                       |     No      |         | No
    interface.lag_port_choices                          |     No      |         | No
    interface.query                                     |     No      |         | No
    interface.rollback                                  |     No      |         | No
    interface.save_default_route                        |     No      |         | No
    interface.services_restarted_on_sync                |     No      |         | No
    interface.update                                    |     No      |         | No
    interface.vlan_parent_interface_choices             |     No      |         | No
    interface.websocket_interface                       |     No      |         | No
    interface.websocket_local_ip                        |     No      |         | No
    interface.xmit_has_policy_choices                   |     No      |         | No
    interface.capabilities.get                          |     No      |         | No
    interface.capabilities.set                          |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize interface manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class IPMIManager:
    """Manages TrueNAS IPMI operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    ipmi.is_loaded                                      |     No      |         | No
    ipmi.chassis.identify                               |     No      |         | No
    ipmi.chassis.info                                   |     No      |         | No
    ipmi.lan.channels                                   |     No      |         | No
    ipmi.lan.get_instance                               |     No      |         | No
    ipmi.lan.query                                      |     No      |         | No
    ipmi.lan.update                                     |     No      |         | No
    ipmi.mc.info                                        |     No      |         | No
    ipmi.sel.clear                                      |     No      |         | Yes
    ipmi.sel.elist                                      |     No      |         | Yes
    ipmi.sel.info                                       |     No      |         | Yes
    ipmi.sensors.query                                  |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize IPMI manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class JBOFManager:
    """Manages TrueNAS JBOF operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    jbof.create                                         |     No      |         | No
    jbof.delete                                         |     No      |         | No
    jbof.get_instance                                   |     No      |         | No
    jbof.licensed                                       |     No      |         | No
    jbof.query                                          |     No      |         | No
    jbof.reapply_config                                 |     No      |         | No
    jbof.update                                         |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize JBOF manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class NetworkManager:
    """Manages TrueNAS Network operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    network.configuration.activity_choices              |     No      |         | No
    network.configuration.config                        |     No      |         | No
    network.configuration.update                        |     No      |         | No
    network.general.summary                             |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize Network manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class RouteManager:
    """Manages TrueNAS route operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    route.ipv4gw_reachable                              |     No      |         | No
    route.system_routes                                 |     No      |         | No
    staticroute.create                                  |     No      |         | No
    staticroute.delete                                  |     No      |         | No
    staticroute.get_instance                            |     No      |         | No
    staticroute.query                                   |     No      |         | No
    staticroute.update                                  |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize route manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class SystemManager:
    """Manages TrueNAS system operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    system.boot_id                                      |     No      |         | No
    system.build_time                                   |     No      |         | No
    system.debug                                        |     No      |         | Yes
    system.feature_enabled                              |     No      |         | No
    system.host_id                                      |     No      |         | No
    system.info                                         |     No      |         | No
    system.is_stable                                    |     No      |         | No
    system.license_update                               |     No      |         | No
    system.product_type                                 |     No      |         | No
    system.ready                                        |     No      |         | No
    system.reboot                                       |     No      |         | Yes
    system.release_notes_url                            |     No      |         | No
    system.shutdown                                     |     No      |         | Yes
    system.state                                        |     No      |         | No
    system.version                                      |     No      |         | No
    system.version_short                                |     No      |         | No
    system.advanced.config                              |     No      |         | No
    system.advanced.get_gpu_pci_choices                 |     No      |         | No
    system.advanced.login_banner                        |     No      |         | No
    system.advanced.sed_global_password                 |     No      |         | No
    system.advanced.sed_global_password_is_set          |     No      |         | No
    system.advanced.serial_port_choices                 |     No      |         | No
    system.advanced.syslog_certificate_authority_choices|     No      |         | No
    system.advanced.syslog_certificate_choices          |     No      |         | No
    system.advanced.update                              |     No      |         | No
    system.advanced.update_gpu_pci_ids                  |     No      |         | No
    system.general.checkin                              |     No      |         | No
    system.general.checkin_waiting                      |     No      |         | No
    system.general.config                               |     No      |         | No
    system.general.country_choices                      |     No      |         | No
    system.general.kbdmap_choices                       |     No      |         | No
    system.general.language_choices                     |     No      |         | No
    system.general.local_url                            |     No      |         | No
    system.general.timezone_choices                     |     No      |         | No
    system.general.ui_address_choices                   |     No      |         | No
    system.general.ui_certificate_choices               |     No      |         | No
    system.general.ui_httpsprotocols_choices            |     No      |         | No
    system.general.ui_restart                           |     No      |         | No
    system.general.ui_v6address_choices                 |     No      |         | No
    system.general.update                               |     No      |         | No
    system.global.id                                    |     No      |         | No
    system.ntpserver.create                             |     No      |         | No
    system.ntpserver.delete                             |     No      |         | No
    system.ntpserver.get_instance                       |     No      |         | No
    system.ntpserver.query                              |     No      |         | No
    system.ntpserver.update                             |     No      |         | No
    system.security.config                              |     No      |         | No
    system.security.update                              |     No      |         | Yes
    system.security.info.fips_available                 |     No      |         | No
    system.security.info.fips_enabled                   |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize system manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class SystemDatasetManager:
    """Manages TrueNAS system dataset operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    systemdataset.config                                |     No      |         | No
    systemdataset.pool_choices                          |     No      |         | No
    systemdataset.update                                |     No      |         | Yes

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize system dataset manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class TrueNASManager:
    """Manages TrueNAS TrueNAS operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    truenas.accept_eula                                 |     No      |         | No
    truenas.get_chassis_hardware                        |     No      |         | No
    truenas.get_customer_information                    |     No      |         | No
    truenas.get_eula                                    |     No      |         | No
    truenas.is_eula_accepted                            |     No      |         | No
    truenas.is_ix_hardware                              |     No      |         | No
    truenas.is_production                               |     No      |         | No
    truenas.managed_by_truecommand                      |     No      |         | No
    truenas.set_production                              |     No      |         | Yes
    truenas.update_customer_information                 |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize TrueNAS manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class TunableManager:
    """Manages TrueNAS tunable operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    tunable.create                                      |     No      |         | Yes
    tunable.delete                                      |     No      |         | Yes
    tunable.get_instance                                |     No      |         | No
    tunable.query                                       |     No      |         | No
    tunable.tunable_type_choices                        |     No      |         | No
    tunable.update                                      |     No      |         | Yes

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize tunable manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class UpdateManager:
    """Manages TrueNAS update operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    update.check_available                              |     No      |         | No
    update.download                                     |     No      |         | Yes
    update.file                                         |     No      |         | Yes
    update.get_auto_download                            |     No      |         | No
    update.get_pending                                  |     No      |         | No
    update.get_trains                                   |     No      |         | No
    update.manual                                       |     No      |         | Yes
    update.set_auto_download                            |     No      |         | No
    update.set_train                                    |     No      |         | No
    update.update                                       |     No      |         | Yes

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize update manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
