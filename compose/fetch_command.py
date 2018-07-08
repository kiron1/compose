
from .fetcher import make_fetcher

def register_fetch_command(subparser):
    parser = subparser.add_parser('fetch', help='Fetch dependencies')
    parser.set_defaults(func=fetch_command)


def fetch_command(workspace, args):
    for dep in workspace.composefile.dependencies:
        dest = workspace.prefix.joinpath('src', dep.name)
        print(':: Fetching {}...'.format(dep.name))
        fetcher = make_fetcher(dep)
        fetcher.fetch(dest)
