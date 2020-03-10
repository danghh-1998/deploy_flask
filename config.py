import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'database.db')}"
SECRET_KEY = 'my_secret_key'

STRING_MAX_LENGTH = 256
TEL_MAX_LENGTH = 10
EMAIL_MAX_LENGTH = 100
