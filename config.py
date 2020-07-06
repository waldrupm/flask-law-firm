import os
from dotenv import load_dotenv

class Config:
  SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
  SQLALCHEMY_TRACK_MODIFICATION = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
  FLASK_APP = os.getenv("FLASK_APP")
  FLASK_ENV = os.getenv("FLASK_ENV")
  SECRET_KEY = os.getenv("SECRET_KEY")