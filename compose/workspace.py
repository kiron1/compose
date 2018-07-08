
import base64
import hashlib
import re
from pathlib import PurePath, Path

from . import constants
from .composefile import Composefile

class Workspace(object):
    def __init__(self, root_dir):
        self._root_dir = Path(root_dir)
        self._composefile = None

    @property
    def root_dir(self):
        return self._root_dir

    @property
    def label(self):
        name = Path(self.root_dir).stem
        sanitized = re.sub(r'[^A-Za-z0-9_.-]', '_', name)[0:42]

        hashed = hashlib.sha256(str(self.root_dir).encode()).digest()[:6]
        encoded_hash = base64.urlsafe_b64encode(hashed).decode()
        return sanitized + '-' + encoded_hash

    @property
    def prefix(self):
        return constants.CACHE_DIR.joinpath(self.label)

    @property
    def composefile(self):
        if self._composefile is not None:
            return self._composefile
        self._composefile = Composefile(self.root_dir.joinpath('Composefile'))
        return self._composefile

def find_workspace_root():
    fsroot = PurePath(Path.cwd().root)
    ret = Path.cwd()
    while PurePath(ret) != fsroot:
        if ret.joinpath('Composefile').is_file(): # pylint: disable=no-member
            return ret
        ret = ret.parent
    return None

def find_workspace():
    wsroot = find_workspace_root()
    assert wsroot is not None, "Could not find workspace"
    return Workspace(wsroot)
