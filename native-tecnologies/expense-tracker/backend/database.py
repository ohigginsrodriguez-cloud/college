import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # read variables from a .env file and sets them in os.environ

try:
    conn = psycopg2.connect(
        f"dbname={os.getenv('DB_NAME')} "
        f"user={os.getenv('DB_USER')} "
        f"host={os.getenv('DB_HOST')} "
        f"password={os.getenv('DB_PASSWORD')} "
        f"port={os.getenv('DB_PORT')} "
    )
    print("Connection succesfull")
except:
    print("I am unable to connect to the database")

# we use a context manager to scope the cursor session
with conn.cursor() as curs:

    try:
        # returns a single row as a tuple
        single_row = curs.fetchone()

        # use an f-string to print the single tuple returned
        print(f"{single_row}")

        # a default install should include this query and some backend workers
        many_rows = curs.fetchmany(5)

        # use the * unpack operator to print many_rows which is a Python list
        print(*many_rows, sep="\n")

    # a more robust way of handling errors
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
