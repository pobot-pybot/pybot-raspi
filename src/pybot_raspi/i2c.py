# -*- coding: utf-8 -*-

__author__ = 'Eric Pascual'

import re


def _get_i2c_bus_id():
    """ Detect i2C bus id depending on the RasPi version

    :return: the id of the detected I2C bus
    :raises Exception: if cannot find one
    """
    for line in open('/proc/cpuinfo').readlines():
        m = re.match('(.*?)\s*:\s*(.*)', line)
        if m:
            name, value = (m.group(1), m.group(2))
            if name == "Revision":
                return 0 if value[-4:] in ('0002', '0003') else 1

    raise Exception('could not determine the I2C bus id')

# Get I2C bus id and initialize the global instance representing it
try:
    import smbus
except ImportError:
    raise NotImplementedError('python-smbus is not installed on this system.')

i2c_bus = smbus.SMBus(_get_i2c_bus_id())
