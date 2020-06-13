#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/flask_test_app')

from flask_test_app import app as application
