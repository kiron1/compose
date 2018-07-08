
from .package import Package

def register_build_command(subparser):
    parser = subparser.add_parser('build', help='Fetch dependencies')
    parser.set_defaults(func=build_command)


def build_command(workspace, args):
    packages = {k.name: k for k in workspace.composefile.dependencies}
    order = workspace.composefile.sorted_dependencies()
    for name in order:
        pkgdesc = packages[name]
        print(':: Building {}...'.format(pkgdesc.name))
        pkg = Package(workspace, pkgdesc)
        builder = pkg.configure()
        builder.build()
        builder.install()
