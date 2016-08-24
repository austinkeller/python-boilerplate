from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from builtins import object

import shutil as _shutil
from tempfile import mkdtemp


class TemporaryDirectory(object):
    """Create and return a temporary directory.  This has the same
    behavior as mkdtemp but can be used as a context manager.  For
    example:

        with TemporaryDirectory() as tmpdir:
            ...

    Upon exiting the context, the directory and everything contained
    in it are removed.
    """

    def __init__(self, suffix=None, prefix=None, dir=None):
        self.name = None  # Handle mkdtemp raising an exception
        self.suffix = suffix
        self.prefix = prefix
        self.dir = dir

    def __repr__(self):
        return "<{} {!r}>".format(self.__class__.__name__, self.name)

    def __enter__(self):
        self.name = mkdtemp(self.suffix, self.prefix, self.dir)
        return self.name

    def __exit__(self, exc, value, tb):
        self.cleanup()

    def cleanup(self, _warn=False):
        _shutil.rmtree(self.name)
