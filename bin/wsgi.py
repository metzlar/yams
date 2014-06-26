'''
VirtualEnv wsgi application

Can be used directly from the web server, this file
will take care of activating the virtualenv.

Assumes YAMS is installed in (env)/src
'''

import os, sys

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.path.pardir
))

activate_this_file = os.path.join(
    PROJECT_ROOT,
    os.path.pardir,
    os.path.pardir,
    'bin',
    'activate_this.py'
)

if os.path.exists(activate_this_file):
    execfile(activate_this_file, dict(__file__=activate_this_file))

sys.path.insert(0, PROJECT_ROOT)

from yams.wsgi import application