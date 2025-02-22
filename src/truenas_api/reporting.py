import logging

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class ReportingManager:
    """Manages TrueNAS reporting operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    reporting.config                                    |     No      |         | No
    reporting.get_data                                  |     No      |         | No
    reporting.graph                                     |     No      |         | No
    reporting.graphs                                    |     No      |         | No
    reporting.netdata_get_data                          |     No      |         | No
    reporting.netdata_graph                             |     No      |         | No
    reporting.netdata_graphs                            |     No      |         | No
    reporting.netdataweb_generate_password              |     No      |         | No
    reporting.update                                    |     No      |         | No
    reporting.exporters.create                          |     No      |         | No
    reporting.exporters.delete                          |     No      |         | No
    reporting.exporters.exporter_schemas                |     No      |         | No
    reporting.exporters.get_instance                    |     No      |         | No
    reporting.exporters.query                           |     No      |         | No
    reporting.exporters.update                          |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize reporting manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
