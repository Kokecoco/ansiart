from ansiart.ansiart import *
try:
    from ._version import version as __version__
except ImportError:
    # _version.pyがない場合、開発中など、バージョンは未定とする
    __version__ = "unknown"