import psycopg2
import psycopg2.extras


from database import get_db
from models import ExpensePost


def add_expense(expense: ExpensePost):
    conn = get_db()

    with conn.cursor() as cur:
        try:
            cur.execute("INSERT INTO expense (name, amount, description, category, date) VALUES (%s, %s, %s, %s, %s) RETURNING expense_id",
                        (expense.name, expense.amount, expense.description, expense.category, expense.date))
            new_id = cur.fetchone()
            conn.commit()

            return new_id[0]
        except Exception:
            conn.rollback()
            raise 
        finally:
            conn.close()

def update_expense(expense_id: int, expense: ExpensePost):
    conn = get_db()

    with conn.cursor() as cur:
        try:
            cur.execute("UPDATE expense SET name = %s, amount = %s, description = %s, category = %s, date = %s WHERE expense_id = %s", 
                        (expense.name, expense.amount, expense.description, expense.category, expense.date, expense_id))
            rows_updated = cur.rowcount
            conn.commit()
            return rows_updated 

        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

def remove_expense(expense_id: int):
    conn = get_db()

    with conn.cursor() as cur:
        try:
            cur.execute("DELETE FROM expense WHERE expense_id = %s", (expense_id,))
            rows_deleted = cur.rowcount
            conn.commit()
            return rows_deleted
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

def get_expenses():
    conn = get_db()

    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as dict_cur:
        try:
            dict_cur.execute("SELECT * FROM expense")
            rows = dict_cur.fetchall()
            list_rows = [dict(row) for row in rows]
            return list_rows 

            raise
        finally:
            conn.close()

def get_expense(expense_id: int):
    conn = get_db()

    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as dict_cur:
        try:
            dict_cur.execute("SELECT * FROM expense WHERE expense_id = %s", (expense_id,))
            row = dict_cur.fetchone()
            if row is None:
                return
            return dict(row)

            raise
        finally:
            conn.close()
