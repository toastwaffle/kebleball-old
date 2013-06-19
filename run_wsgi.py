import os, sys

dir = os.getcwd()

activate_this = '/'.join(dir,'bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

sys.path.append(0, dir)

from tickets import app as application
