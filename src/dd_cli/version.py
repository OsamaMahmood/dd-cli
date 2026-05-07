from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("dd-cli")
except PackageNotFoundError:
    __version__ = "0.0.0+local"
