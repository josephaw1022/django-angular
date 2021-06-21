
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = str(os.getenv('SECRET_KEY'))
