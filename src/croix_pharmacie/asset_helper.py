import importlib.resources
from pathlib import Path

PATH_PACKAGE = "croix_pharmacie.assets"

def get_asset_path(file_name: str, subdirs: str | None = None) -> Path:
    if subdirs:
        package = f"{PATH_PACKAGE}.{subdirs}"
    with importlib.resources.path(package, file_name) as path:
        return path