
from subprocess import run

class GitFetcher(object):
    def __init__(self, package_desc):
        self._package_desc = package_desc

    def fetch(self, location):
        if not location.joinpath('.git', 'config').is_file():
            location.mkdir(parents=True, exist_ok=True)
            cmd = ['git', 'clone', self.package_desc.src_uri, location]
            run(cmd, cwd=location)
        return location

    @property
    def package_desc(self):
        return self._package_desc
