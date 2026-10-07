from database import get_db
import psycopg2
from decimal import Decimal
from datetime import date


def add_expense(name: str, amount: Decimal, category: str, date: date, description: str | None = None):
    conn = get_db()

    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO expense (name, amount, description, category, date) VALUES (%s, %s, %s, %s, %s) RETURNING expense_id",(name, amount, description, category, date))
            expense = cur.fetchone()
            conn.commit()

            return expense[0]
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()
        finally:
            conn.close()
            
def update_expense(expense_id: int, name: str, amount: Decimal, category: str, date: date, description: str | None = None):
    conn = get_db()

    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE expense SET name = %s, amount = %s, description = %s, category = %s, date = %s WHERE expense_id = %s", (name, amount, description, category, date, expense_id))
            conn.commit()

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()
        finally:
            conn.close()

def remove_expense(expense_id: int):
    conn = get_db()

    with conn.cursor() as cur:
        try:
            cur.execute("DELETE FROM expense WHERE expense_id = %s", (expense_id,))
            conn.commit()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()
        finally:
            conn.close()

def get_expenses():
    conn = get_db()

    with conn.cursor() as cur:
        try:
            cur.execute("SELECT * FROM expense")
            rows = cur.fetchall()
            print(*rows, sep="\n")
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
            print(row)  
            return row
        
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()

if __name__ == "__main__":
    new_id = add_expense("gym", 500, "salud", date.today())
    get_expenses()
    get_expense(new_id)
    update_expense(new_id, "gymmmm", 499, "health" ,date.today())
    get_expense(new_id)
    remove_expense(new_id)
    get_expenses()
