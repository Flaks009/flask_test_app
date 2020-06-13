#flaskapp.wsgi
import sys
sys.path.insert(0, '/var/www/html/flask_test_app')

from flaskapp import app as application
