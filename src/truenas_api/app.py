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
