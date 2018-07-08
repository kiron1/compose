
def register_install_command(subparser):
    parser = subparser.add_parser('install', help='Install new dependency')
    parser.add_argument('-n', '--name', help='Name')
    parser.add_argument('-u', '--src', help='Source URI')
    parser.add_argument('-k', '--kind', choices=['cmake', 'autoconf'], default='cmake', help='Package Kind')
    parser.set_defaults(func=install_command)


def install_command(workspace, args):
    assert args.name not in workspace.composefile, 'Dependency already known'
    workspace.composefile[args.name] = {}
    workspace.composefile[args.name]['src_uri'] = args.src
    workspace.composefile[args.name]['kind'] = args.kind
    workspace.composefile.save()
