import logging
from typing import Any, Dict, Optional

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class AppManager:
    """Manages application operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    app.available                                       |     No      |         | No
    app.available_space                                 |     No      |         | No
    app.categories                                      |     No      |         | No
    app.certificate_authority_choices                   |     No      |         | No
    app.certificate_choices                             |     No      |         | No
    app.config                                          |     No      |         | No
    app.container_console_choices                       |     No      |         | No
    app.container_ids                                   |     No      |         | No
    app.convert_to_custom                               |     No      |         | Yes
    app.create                                          |     No      |         | Yes
    app.delete                                          |     No      |         | Yes
    app.get_instance                                    |     No      |         | No
    app.gpu_choices                                     |     No      |         | No
    app.ip_choices                                      |     No      |         | No
    app.latest                                          |     No      |         | No
    app.outdated_docker_images                          |     No      |         | No
    app.pull_images                                     |     No      |         | Yes
    app.query                                           |     No      |         | No
    app.redeploy                                        |     No      |         | Yes
    app.rollback                                        |     No      |         | Yes
    app.rollback_versions                               |     No      |         | No
    app.similar                                         |     No      |         | No
    app.start                                           |     No      |         | Yes
    app.stop                                            |     No      |         | Yes
    app.update                                          |     No      |         | Yes
    app.upgrade                                         |     No      |         | Yes
    app.upgrade_summary                                 |     No      |         | No
    app.used_ports                                      |     No      |         | No
    app.ix_volume.exists                                |     No      |         | No
    app.ix_volume.query                                 |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize application manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class AppImageManager:
    """Manages application image operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    app.image.delete                                    |     No      |         | No
    app.image.dockerhub_rate_limit                      |     No      |         | No
    app.image.get_instance                              |     No      |         | No
    app.image.pull                                      |     No      |         | Yes
    app.image.query                                     |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize application image manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class AppCatalogManager:
    """Manages application catalog operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    catalog.apps                                        |     No      |         | No
    catalog.config                                      |     No      |         | No
    catalog.get_app_details                             |     No      |         | No
    catalog.sync                                        |     No      |         | Yes
    catalog.trains                                      |     No      |         | No
    catalog.update                                      |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize applicaiton catalog manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class DockerManager:
    """Manages authentication operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    docker.config                                       |     No      |         | No
    docker.nvidia_present                               |     No      |         | No
    docker.status                                       |     No      |         | No
    docker.update                                       |     No      |         | Yes
    docker.network.get_instance                         |     No      |         | No
    docker.network.query                                |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize docker manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...


class K8sToDockerManager:
    """Manages TrueNAS k8s_to_docker operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    k8s_to_docker.list_backups                          |     No      |         | Yes
    k8s_to_docker.migrate                               |     No      |         | Yes

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize k8s_to_docker manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection


class VMManager:
    """Manages TrueNAS VM operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    vm.bootloader_options                               |     No      |         | No
    vm.bootloader_ovmf_choices                          |     No      |         | No
    vm.clone                                            |     No      |         | No
    vm.cpu_model_choices                                |     No      |         | No
    vm.create                                           |     No      |         | No
    vm.delete                                           |     No      |         | No
    vm.export_disk_image                                |     No      |         | Yes
    vm.flags                                            |     No      |         | No
    vm.get_available_memory                             |     No      |         | No
    vm.get_console                                      |     No      |         | No
    vm.get_display_devices                              |     No      |         | No
    vm.get_display_web_url                              |     No      |         | No
    vm.get_instance                                     |     No      |         | No
    vm.get_memory_usage                                 |     No      |         | No
    vm.get_vm_memory_info                               |     No      |         | No
    vm.get_vmemory_in_use                               |     No      |         | No
    vm.guest_architecture_and_machine_choices           |     No      |         | No
    vm.import_disk_image                                |     No      |         | Yes
    vm.log_file_download                                |     No      |         | Yes
    vm.log_file_path                                    |     No      |         | No
    vm.maximum_supported_vcpus                          |     No      |         | No
    vm.port_wizard                                      |     No      |         | No
    vm.poweroff                                         |     No      |         | No
    vm.profiles                                         |     No      |         | No
    vm.query                                            |     No      |         | No
    vm.random_mac                                       |     No      |         | No
    vm.resolution_choices                               |     No      |         | No
    vm.restart                                          |     No      |         | Yes
    vm.resume                                           |     No      |         | No
    vm.start                                            |     No      |         | No
    vm.status                                           |     No      |         | No
    vm.stop                                             |     No      |         | Yes
    vm.supports_virtualization                          |     No      |         | No
    vm.suspend                                          |     No      |         | No
    vm.update                                           |     No      |         | No
    vm.virtualization_details                           |     No      |         | No
    vm.device.bind_choices                              |     No      |         | No
    vm.device.create                                    |     No      |         | No
    vm.device.delete                                    |     No      |         | No
    vm.device.disk_choices                              |     No      |         | No
    vm.device.get_instance                              |     No      |         | No
    vm.device.get_pci_ids_for_gpu_isolation             |     No      |         | No
    vm.device.iommu_enabled                             |     No      |         | No
    vm.device.iotype_choices                            |     No      |         | No
    vm.device.nic_attach_choices                        |     No      |         | No
    vm.device.passthrough_device                        |     No      |         | No
    vm.device.passthrough_device_choices                |     No      |         | No
    vm.device.pptdev_choices                            |     No      |         | No
    vm.device.query                                     |     No      |         | No
    vm.device.update                                    |     No      |         | No
    vm.device.usb_controller_choices                    |     No      |         | No
    vm.device.usb_passthrough_choices                   |     No      |         | No
    vm.device.usb_passthrough_device                    |     No      |         | No
    vm.device.update                                    |     No      |         | No
    vm.device.update                                    |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize VM manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
