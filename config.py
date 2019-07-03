import os

from flask import Flask

#WEB_ADDRESS ='0.0.0.0'
WEB_ADDRESS ='192.168.103'
WEB_PORT = 5000
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(PROJECT_ROOT, 'jotoapp/templates')
STATIC_FOLDER = os.path.join(PROJECT_ROOT, 'jotoapp/static')
DEBUG = False
LOG_FILE = 'pytell.log'


app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC_FOLDER)

if DEBUG:
    app.debug = DEBUG
