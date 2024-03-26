import logging
from importlib import import_module

from . import base

logger = logging.getLogger(__name__)

INSTALLED_APPS = [*base.INSTALLED_APPS]
DEV_APPS: list[str] = ["django_extensions"]


for app in DEV_APPS:
    try:
        import_module(app)
        INSTALLED_APPS.append(app)
    except ImportError:
        logger.log(logging.WARN, "Unable to load %s", app)
