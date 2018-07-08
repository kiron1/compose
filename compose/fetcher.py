
from .git_fetcher import GitFetcher

class Fetcher(object):
    def __init__(self, package_desc):
        self._package_desc = package_desc

    def fetch(self, destination):
        pass

def make_fetcher(package_desc):
    src_uri = package_desc.src_uri
    if src_uri.endswith('.git'):
        return GitFetcher(package_desc)
    elif src_uri.startswith('http://') or src_uri.startswith('https://'):
        #return HttpFetcher(package_desc)
        raise NotImplementedError
    #return FileFetcher(package_desc)
    raise NotImplementedError
