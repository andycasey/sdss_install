# License information goes here
# -*- coding: utf-8 -*-
"""
================
sdss4tools.install
================

This package contains code for installing SDSS-IV software products.
"""
from __future__ import absolute_import, division, print_function, unicode_literals
# The line above will help with 2to3 support.

from .install import Install
from .modules import Modules
from .get_svn_devstr import get_svn_devstr
from .most_recent_tag import most_recent_tag
from .version import version

