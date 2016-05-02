# -*- coding: utf-8 -*-

""" Specific stuff useful when targeting a RaspberyPi
"""

import os

# make it possible to import this module on non-RasPi platform when generating documentation
if 'AUTO_DOC' not in os.environ:
    import platform
    if not platform.machine().startswith('armv'):
        raise ImportError('can be imported on Raspberry Pi only')

    from .i2c import *

else:
    i2c_bus = None
