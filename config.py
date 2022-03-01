from dotenv import load_dotenv
import os 
basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()
class Config(object):
    SECRET_KEY = 'top-secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = 'jwt-secret'