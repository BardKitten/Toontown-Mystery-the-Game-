"Python bindings for the Panda3D libraries"

import os

bindir = os.path.join(os.path.dirname(__file__), '..', 'bin')
if os.path.isfile(os.path.join(bindir, 'libpanda.dll')):
    if not os.environ.get('PATH'):
        os.environ['PATH'] = bindir
    else:
        os.environ['PATH'] = bindir + os.pathsep + os.environ['PATH']

del os, bindir
