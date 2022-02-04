from .imbalance import *
from .target import *
from .utils import *
from .feature import *


from pkg_resources import get_distribution, DistributionNotFound
try:
    VERSION = get_distribution(__name__).version
except DistributionNotFound:
    try:
        from ._version import version as VERSION
    except ImportError:
        raise ImportError(
            "Failed to find (autogenerated) _version.py. "
            "This might be because you are installing from GitHub's tarballs, "
            "use the PyPI ones."
            )
__version__ = VERSION