import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Supersecret'

    # Database
    SQLALCHEMY_DATABASE_URI = 'postgres://bflaks:181095@localhost/test_db'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False