from database import get_db
import psycopg2
from decimal import Decimal
from datetime import date


def add_expense(name: str, amount: Decimal, category: str, date: date, description: str | None = None):
    conn = get_db()

    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO expense (name, amount, description, category, date) VALUES (%s, %s, %s, %s, %s) RETURNING expense_id",(name, amount, description, category, date))
            conn.commit()

            return 
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()
            
def update_expense():
    pass

def remove_expense(expense_id: int):
    conn = get_db()

    with conn.cursor() as cur:
        try:
            cur.execute("DELETE FROM expense WHERE expense_id = %s", (expense_id,))
            conn.commit()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()

def get_expenses():
    conn = get_db()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT * FROM expense")
            rows = cur.fetchall()
            return rows
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()

def get_expense(expense_id: int):
    conn = get_db()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT * FROM expense WHERE expense_id = %s", (expense_id,))
            row = cur.fetchone()
            return row
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()
