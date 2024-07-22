import os

import pandas as pd

from oci_ai_code_academy import settings

import logging
from logging.config import dictConfig
dictConfig(settings.LOG_CONFIG)
logger = logging.getLogger(__name__)