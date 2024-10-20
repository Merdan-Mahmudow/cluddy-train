from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_NAME = os.getenv("DB_NAME")
DB_PASS = os.getenv("DB_PASS")



SECRET_KEY = os.getenv("SECRET_KEY")
API_KEY = os.getenv("API_KEY")
SHOP_ID = os.getenv("SHOP_ID")