"""
database.py

Contains classes for database table objects
"""

from flask.ext.sqlalchemy import SQLAlchemy
from tickets import app
from tickets.helpers import *
import bcrypt

db = SQLAlchemy(app)

from affiliation import Affiliation
from announcement import Announcement
from battels_auto import Battels_auto
from battels_manual import Battels_manual
from college import College
from log import Log
from statistic import Statistic
from ticket import Ticket
from user import User
from voucher import Voucher
