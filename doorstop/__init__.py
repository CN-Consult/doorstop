# SPDX-License-Identifier: LGPL-3.0-only

"""Package for doorstop."""

from importlib.metadata import PackageNotFoundError, version

from doorstop.common import DoorstopError, DoorstopInfo, DoorstopWarning
from doorstop.core import (
    Document,
    Item,
    Tree,
    build,
    builder,
    editor,
    exporter,
    find_document,
    find_item,
    importer,
    publisher,
)

from pathlib import Path

__project__ = "Doorstop"

# Prefer the source tree version (pyproject) when available, otherwise fall
# back to the installed package metadata, then to a local marker.
_pyproject_version = None
_pyproject_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
if _pyproject_path.is_file():
    try:
        try:
            import tomllib  # type: ignore
        except ImportError:  # pragma: no cover - Python <3.11
            import tomli as tomllib  # type: ignore
        data = tomllib.loads(_pyproject_path.read_text())
        _pyproject_version = data.get("tool", {}).get("poetry", {}).get("version")
    except Exception:  # pragma: no cover - non-critical fallback
        _pyproject_version = None

if _pyproject_version:
    __version__ = _pyproject_version
else:
    try:
        __version__ = version("doorstop")
    except PackageNotFoundError:
        __version__ = "(local)"

CLI = "doorstop"
GUI = "doorstop-gui"
SERVER = "doorstop-server"
VERSION = "{0} v{1}".format(__project__, __version__)
DESCRIPTION = "Requirements management using version control."
