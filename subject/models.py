from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

db = SQLAlchemy(app)
Migrate(app,db)
class Subject(db.Model):

    __tablename__ = 'subjects'

    id = db.Column(db.Integer, primary_key=True)
    teacher=db.Column(db.Text)
    subject = db.Column(db.Text)
    date = db.Column(db.Text)
    comment = db.Column(db.Text)
    exam=db.Column(db.Text)
    exammid=db.Column(db.Text)
    datemid=db.Column(db.Text)

    def __init__(self,teacher,subject, date, comment,exam,exammid,datemid):
        self.teacher =teacher
        self.subject = subject

        self.date = date
        self.comment = comment
        self.exam=exam
        self.exammid=exammid
        self.datemid=datemid







