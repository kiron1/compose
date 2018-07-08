#!/usr/bin/evn python3

import sys
import argparse

from . import workspace
from .build_command import register_build_command
from .clean_command import register_clean_command
from .fetch_command import register_fetch_command
from .install_command import register_install_command

def _argparse(argv):
    parser = argparse.ArgumentParser(description='Composer')
    parser.add_argument('--venv', default=False, action='store_true', help='Show virtual environment path')
    subparser = parser.add_subparsers(help='sub-command help')

    register_build_command(subparser)
    register_clean_command(subparser)
    register_fetch_command(subparser)
    register_install_command(subparser)

    return parser.parse_args(argv[1:])

def main(argv):
    args = _argparse(argv)
    ws = workspace.find_workspace()
    assert ws is not None, 'Workspace not found'
    if args.venv:
        print(ws.prefix)
        return 0

    rc = args.func(ws, args)
    return rc

if __name__ == '__main__':
    sys.exit(main(sys.argv))
