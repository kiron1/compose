
import os
from pathlib import Path

def _mk_xdg_path(name, default):
    p = Path(os.environ.get(name, default))
    return p.expanduser().joinpath('composer')

CONFIG_DIR = _mk_xdg_path('XDG_CONFIG_HOME', '~/.config')
CACHE_DIR = _mk_xdg_path('XDG_CACHE_HOME', '~/.cache')
DATA_DIR = _mk_xdg_path('XDG_DATA_HOME', '~/.local/share')
