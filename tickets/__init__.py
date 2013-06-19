from flask import Flask, session, redirect, url_for, escape, request, render_template, send_from_directory, flash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://kebleball:E9R8h22SnyGrFN3b@localhost/kebleball'
app.secret_key = b'\x95\xe0\x18+\x12\xb6\xd9\x8f\xec\xace\xf4\xe6\xd8\x8dB\x14\x0b4C\x83\xde\xce\x90'

#from tickets.database import *
from tickets.views import *
from tickets.helpers import *
