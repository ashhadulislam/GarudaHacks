# print("At app factory")
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# app = Flask(__name__)
# app.config.from_object(os.environ.get('APP_SETTINGS', DevelopmentConfig))
# app.secret_key = app.config['SECRET_KEY']
# db = SQLAlchemy(app)

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# print("End of  app factory")

