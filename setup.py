#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='pybot_raspi',
      namespace_packages=['pybot'],
      version='1.0',
      description='PyBot extension for Raspberry Pi support',
      install_requires=['pybot_core'],
      license='LGPL',
      author='Eric Pascual',
      author_email='eric@pobot.org',
      url='http://www.pobot.org',
      download_url='https://github.com/Pobot/PyBot',
      packages=find_packages("src"),
      package_dir={'': 'src'}
      )
