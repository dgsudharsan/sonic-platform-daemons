import os
import sys
from imp import load_source  # Replace with importlib once we no longer need to support Python 2

import pytest

# TODO: Clean this up once we no longer need to support Python 2
if sys.version_info >= (3, 3):
    from unittest.mock import MagicMock, patch, mock_open
else:
    from mock import MagicMock, patch, mock_open

from .mock_platform import MockStorageDevice

tests_path = os.path.dirname(os.path.abspath(__file__))

# Add mocked_libs path so that the file under test can load mocked modules from there
mocked_libs_path = os.path.join(tests_path, "mocked_libs")
sys.path.insert(0, mocked_libs_path)
from sonic_py_common import daemon_base, device_info

# Add path to the file under test so that we can load it
modules_path = os.path.dirname(tests_path)
scripts_path = os.path.join(modules_path, "scripts")
sys.path.insert(0, modules_path)
load_source('stormond', os.path.join(scripts_path, 'stormond'))
import stormond


daemon_base.db_connect = MagicMock()

SYSLOG_IDENTIFIER = 'storagedevice_test'
NOT_AVAILABLE = 'N/A'