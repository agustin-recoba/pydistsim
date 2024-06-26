# Readthedocs default blue theme
html_style = None

# Mock modules that are not present on readthedocs
# http://read-the-docs.readthedocs.org/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules
import sys


class Mock:
    def __init__(self, *args, **kwargs):
        pass

    def __call__(self, *args, **kwargs):
        return Mock()

    @classmethod
    def __getattr__(cls, name):
        if name in ("__file__", "__path__"):
            return "/dev/null"
        elif name[0] == name[0].upper():
            mockType = type(name, (), {})
            mockType.__module__ = __name__
            return mockType
        else:
            return Mock()

    def __or__(self, other):
        return Mock()


MOCK_MODULES = [
    "networkx",
    "png",
    "PySide6",
    "PySide6.QtCore",
    "PySide6.QtGui",
    "scipy",
    "scipy.stats",
    "loguru",
]
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()
