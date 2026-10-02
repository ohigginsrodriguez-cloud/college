from database import get_db
import psycopg2


def get_expenses():
    try:
        conn = get_db()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    with conn.cursor() as curs:
        try:
            return rows = curs.fetchall()
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

def get_expense():
    try:
        conn = get_db()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    with conn.cursor() as curs:
        try:
            return rows = curs.fetchone()
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

get_expense()   
get_expenses()
