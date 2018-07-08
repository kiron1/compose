
import configparser
from pathlib import Path
from .package_desc import PackageDesc

class Composefile(configparser.ConfigParser): # pylint: disable=too-many-ancestors
    def __init__(self, file_path):
        configparser.ConfigParser.__init__(self)
        self._file_path = Path(file_path)
        self.read(file_path)

    def save(self):
        with open(self.file_path, 'w') as configfile:
            self.write(configfile)

    @property
    def file_path(self):
        return self._file_path

    @property
    def dependencies(self):
        for sec in self.sections():
            if sec == 'this':
                continue
            src_uri = self[sec].get('src_uri', '')
            depends = self[sec].get('depends', '').split()
            yield PackageDesc(src_uri, name=sec, depends=depends)

    def sorted_dependencies(self):
        leaf_nodes = list()
        dependencies = list()
        for d in self.dependencies:
            print(d)
            if not d.depends:
                leaf_nodes.append(d)
            else:
                dependencies.append(d)

        result = list()

        while leaf_nodes:
            n = leaf_nodes.pop()
            result.append(n.name)
            for d in dependencies:
                if n.name in d.depends:
                    d.depends.remove(n.name)
                    if not d.depends:
                        leaf_nodes.append(d)
        return result
