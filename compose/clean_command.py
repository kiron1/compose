
from shutil import rmtree

def register_clean_command(subparser):
    parser = subparser.add_parser('clean', help='Clean up')
    parser.set_defaults(func=clean_command)


def clean_command(workspace, args):
    prefix = workspace.prefix
    print(':: Cleaning {}...'.format(prefix))
    if prefix.exists():
        rmtree(prefix)
    return 0
