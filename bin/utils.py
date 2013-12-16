#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import errno
import os
import platform
import shutil
import sys


def create_dir(path):
    """Creates a directory atomically."""
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def decode(string):
    """Converts byte string to Unicode string."""
    if is_python2():
        return string.decode('utf-8', errors='replace')
    return string


def encode(string):
    """Converts Unicode string to byte string."""
    if is_python2():
        return string.encode('utf-8', errors='replace')
    return string


def encode_local(string, encoding=None):
    """Converts string into local filesystem encoding."""
    if is_python2():
        return decode(string).encode(encoding or sys.getfilesystemencoding())
    return string


def is_python2():
    return sys.version_info[0] == 2


def is_linux():
    return platform.system() == 'Linux'


def is_osx():
    return platform.system() == 'Darwin'


def is_windows():
    return platform.system() == 'Windows'


def move_file(src, dst):
    """
    Atomically move file.

    Windows does not allow for atomic file renaming (which is used by
    os.rename / shutil.move) so destination paths must first be deleted.
    """
    if is_windows() and os.path.exists(dst):
        # raises exception if file is in use on Windows
        os.remove(dst)
    shutil.move(src, dst)