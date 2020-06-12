import os

class Config(object):
    #key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Supersecret'

    #upload
    UPLOAD_FOLDER = 'uploads/'
    ALLOWED_EXTENSIONS = {'txt', 'csv'}
