#! /usr/bin/env python3
import os, sys

dir = os.getcwd()

activate_this = os.path.join(dir,'bin/activate_this.py')
with open(activate_this, 'r') as fh:
    exec(fh.read()+'\n', dict(__file__=activate_this), sys._getframe(0).f_locals)

from tickets import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
