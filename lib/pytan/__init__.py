# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4
# Please do not change the two lines above. See PEP 8, PEP 263.
'''
PyTan Description
=================

A Python library that provides a simple way for programmatically interfacing
with Tanium's SOAP API. It is comprised of three parts:

-  TaniumPy API: A set of Python objects that are automatically generated
   from the WSDL that describes the Tanium SOAP API.
-  PyTan Handler API: An API that makes the objects exposed by TaniumPy
   easier to use.
-  PyTan Command Line Scripts: A set of command line scripts that utilize
   the PyTan Handler API to make it easy for non-programmers to utilize the
   Tanium SOAP API to create/get/delete/ask/deploy objects.

.. Why_PyTan_was_created:

Why PyTan was created
=====================

PyTan was created to solve for the following needs:

-  Create a python library to provide an easy set of methods for
   programmatically interfacing with Tanium via the SOAP API
-  Create a set of command line scripts utilizing the python library created
   above that handle the argument parsing, thereby providing non-python users
   with command line access to the functionality provided by the methods
   inside of the python library
-  Provide a way to ask questions and get results via Python and/or the
   command line.
-  Provide a way to deploy actions and get results via Python and/or the
   command line.
-  Provide a way to export/import objects in JSON via Python and/or the
   command line.

.. Requirements:

Requirements
============
-  Python 2.7
-  A working install of Tanium Server 6.2

.. Installation:

Installation
============

Windows Installation
    * Download Python 2.7 from https://www.python.org/downloads/windows/
    * Install Python 2.7 -- if you accept the default paths it will install
      to C:\Python27
    * Copy PyTan from github to your local machine somewhere
    * If you did not accept the default install path for Python 2.7, edit
      ``pytan\winbin\CONFIG.bat`` to change the *PYTHON* variable to point
      to the full path of *python.exe*

OS X Installation
    * OS X 10.8 and higher come with Python 2.7 out of the box
    * Copy PyTan from github to your local machine somewhere

Linux Installation
    * Ensure Python 2.7 is installed
    * Ensure the first *python* binary in your path points to your Python 2.7
      installation
    * Copy PyTan from github to your local machine somewhere

.. API Usage:

API Usage
============

See :mod:`pytan.handler` submodule for API Usage


'''

__title__ = 'PyTan'
__version__ = '1.0.0'
__author__ = 'Jim Olsen <jim.olsen@tanium.com>'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Tanium'

import sys
import os

# disable python from creating .pyc files everywhere
sys.dont_write_bytecode = True

my_file = os.path.abspath(__file__)
my_dir = os.path.dirname(my_file)
parent_dir = os.path.dirname(my_dir)
path_adds = [parent_dir]

for aa in path_adds:
    if aa not in sys.path:
        sys.path.append(aa)

import pytan  # noqa
import taniumpy  # noqa
from pytan.handler import Handler  # noqa
from pytan import utils  # noqa
from pytan import constants  # noqa

# Set default logging handler to avoid "No handler found" warnings.
import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())