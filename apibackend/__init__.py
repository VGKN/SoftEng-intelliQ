## This file is ran automatically the first time a Python program imports the package dbdemo
from flask import Flask
from flask_mysqldb import MySQL
import json

#The UPLOAD_FOLDER is where we will store the uploaded files
# the ALLOWED_EXTENSIONS is the set of allowed file extensions.
UPLOAD_FOLDER = './apibackend/'
ALLOWED_EXTENSIONS = {'json', 'csv'}



## __name__ is the name of the module. When running directly from python, it will be 'dbdemo'
## Outside of this module, as in run.py, it is '__main__' by default
## Create an instance of the Flask class to be used for request routing
app = Flask(__name__, template_folder= '../frontend/templates')

## configuration of database

app.config.from_file("config.json",load=json.load)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_SORT_KEYS'] = False

## secret key for sessions (signed cookies). Flask uses it to protect the contents of the user session against tampering.
## token for csrf protection of forms.
## secret keys can be generated by secrets.token_hex()

## initialize database connection object
db = MySQL(app)

## routes must be imported after the app object has been initialized
from apibackend import routes