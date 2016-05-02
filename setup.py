#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from git_version import git_version

setup(name='pybot-raspi',
      namespace_packages=['pybot'],
      version=git_version(),
      description='PyBot extension for Raspberry Pi support',
      install_requires=['pybot-core'],
      license='LGPL',
      author='Eric Pascual',
      author_email='eric@pobot.org',
      url='http://www.pobot.org',
      download_url='https://github.com/Pobot/PyBot',
      packages=find_packages("src"),
      package_dir={'': 'src'}
      )
