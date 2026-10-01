import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # read variables from a .env file and sets them in os.environ

def get_db():
    return psycopg2.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
            )

db = get_db()
if db: 
    print("Connection succesfull")
