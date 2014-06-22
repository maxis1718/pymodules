#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name = 'pymodules',
	version = '2.0',
	author="Maxis Kao",
	url="http://maxis1718.github.io",
	author_email="maxis1718@gmail.com",
	py_modules = ['dependency','color','ListCombination','mathutil','mongo','sqlitedb','timer'],
	)