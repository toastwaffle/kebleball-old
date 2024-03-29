"""
college.py

Contains College class
Used to associate users with their colleges
"""

from tickets.database import db

class College(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<College {id}: {name}>".format_map(vars(self))