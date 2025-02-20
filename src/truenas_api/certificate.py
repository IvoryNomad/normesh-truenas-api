import logging
from typing import Any, Dict, Optional

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class CertificateManager:
    """Manages certificate operations via TrueNAS WebSocket API

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    certificate.acme_server_choices                     |     No      |         | No
    certificate.certificate_signing_request_profiles    |     No      |         | No
    certificate.country_choices                         |     No      |         | No
    certificate.create                                  |     No      |         | Yes
    certificate.delete                                  |     No      |         | Yes
    certificate.ec_curve_choices                        |     No      |         | No
    certificate.extended_key_usage_choices              |     No      |         | No
    certificate.get_instance                            |     No      |         | No
    certificate.key_type_choices                        |     No      |         | No
    certificate.profiles                                |     No      |         | No
    certificate.query                                   |     No      |         | No
    certificate.update                                  |     No      |         | Yes
    certificateauthority.ca_sign_csr                    |     No      |         | No
    certificateauthority.create                         |     No      |         | No
    certificateauthority.delete                         |     No      |         | No
    certificateauthority.get_instance                   |     No      |         | No
    certificateauthority.profiles                       |     No      |         | No
    certificateauthority.query                          |     No      |         | No
    certificateauthority.update                         |     No      |         | No
    certificateauthority.create                         |     No      |         | No

    """

    def __init__(self, connection: TrueNASConnection):
        """Initialize cretificate manager.

        Args:
            connection: Authenticated TrueNAS connection
        """
        self.conn = connection
        ...
