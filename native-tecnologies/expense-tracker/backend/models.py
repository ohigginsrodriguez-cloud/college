from pydantic import BaseModel, Field
from datetime import date
from decimal import Decimal


class Expense(BaseModel):
    name: str
    amount: Decimal
    description: str | None = None
    category: str
    date: date

class ExpensePost(Expense):
    pass

class ExpenseGet(Expense):
    expense_id: int
  
class ExpensePut(Expense):
    expense_id: int
