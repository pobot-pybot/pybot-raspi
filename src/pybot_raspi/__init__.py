# -*- coding: utf-8 -*-

import platform
if not platform.machine().startswith('armv6'):
    raise ImportError('can be imported on Raspberry Pi only')

from .i2c import *
