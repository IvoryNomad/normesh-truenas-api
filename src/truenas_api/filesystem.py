import logging

from .connection import TrueNASConnection, TrueNASResponse

logger = logging.getLogger(__name__)


class FilesystemManager:
    """Manage TrueNAS filesystem operations via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    filesystem.acl_is_trivial                           |     No      |         | No
    filesystem.can_access_as_user                       |     No      |         | No
    filesystem.chown                                    |     No      |  0.1.0  | Yes
    filesystem.default_acl_choices                      |     No      |         | No
    filesystem.get                                      |     No      |         | Yes
    filesystem.get_default_acl                          |     No      |         | No
    filesystem.get_zfs_attributes                       |     No      |         | No
    filesystem.get_acl                                  |     No      |         | No
    filesystem.is_immutable                             |     No      |         | No
    filesystem.listdir                                  |     No      |  0.1.0  | No
    filesystem.mkdir                                    |     No      |  0.1.0  | No
    filesystem.put                                      |     No      |         | Yes
    filesystem.set_immutable                            |     No      |         | No
    filesystem.set_zfs_attributes                       |     No      |         | No
    filesystem.setacl                                   |     No      |         | Yes
    filesystem.setperm                                  |     No      |  0.1.0  | Yes
    filesystem.stat                                     |     No      |  0.1.0  | No
    filesystem.statfs                                   |     No      |  0.1.0  | No

    """


class FSACLManager:
    """Manage filesystem ACL templates via TrueNAS WebSocket API.

    Available methods                                   | implemented | planned | Job?
    ----------------------------------------------------+-------------+---------+------
    filesystem.acltemplate.by_path                      |     No      |         | No
    filesystem.acltemplate.create                       |     No      |         | No
    filesystem.acltemplate.delete                       |     No      |         | No
    filesystem.acltemplate.get_instance                 |     No      |         | No
    filesystem.acltemplate.query                        |     No      |         | No
    filesystem.acltemplate.update                       |     No      |         | No

    """
