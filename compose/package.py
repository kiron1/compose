
from subprocess import run

class CMakeBuilder(object):
    def __init__(self, package):
        self._package = package
        self._configure()

    def _configure(self):
        self.binary_dir.mkdir(parents=True, exist_ok=True)
        cmd = [
            'cmake',
            '-DCMAKE_PREFIX_PATH={}'.format(self.prefix),
            self.package.source_dir
        ]
        print(':: Configure {}'.format(' '.join([str(k) for k in cmd])))
        run(cmd, cwd=self.binary_dir)

    def build(self):
        cmd = ['cmake', '--build', self.binary_dir]
        print(cmd)
        print(':: Build {}'.format(' '.join([str(k) for k in cmd])))
        run(cmd, cwd=self.binary_dir)

    def install(self):
        cmd = [
            'cmake',
            #'-DCMAKE_INSTALL_CONFIG_NAME={}',
            '-DCMAKE_INSTALL_PREFIX={}'.format(self.prefix),
            '-P',
            str(self.binary_dir.joinpath('cmake_install.cmake')),
        ]
        print(':: Install {}'.format(' '.join([str(k) for k in cmd])))
        run(cmd, cwd=self.binary_dir)

    @property
    def package(self):
        return self._package

    @property
    def binary_dir(self):
        return self._package.binary_dir

    @property
    def source_dir(self):
        return self._package.source_dir

    @property
    def prefix(self):
        return self._package.workspace.prefix

class Package(object):
    def __init__(self, workspace, pkgdesc):
        self._workspace = workspace
        self._pkgdesc = pkgdesc

    def configure(self): # TODO: config
        print(self.source_dir)
        assert self.source_dir.joinpath('CMakeLists.txt').exists(), 'Only CMake supported right now'
        return CMakeBuilder(self)

    @property
    def workspace(self):
        return self._workspace

    @property
    def source_dir(self):
        return self.workspace.prefix.joinpath('src', self._pkgdesc.name)

    @property
    def binary_dir(self):
        return self.workspace.prefix.joinpath('src', '{}-build'.format(self._pkgdesc.name))
