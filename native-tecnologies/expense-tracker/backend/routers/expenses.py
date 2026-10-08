from fastapi import APIRouter
from crud import add_expense, get_expenses, get_expense, update_expense, remove_expense
from models import ExpensePost, ExpenseGet, ExpensePut


router = APIRouter(
        prefix="/expenses",
        tags=["expenses"],
        responses={404: {"description": "Not found"}},
        )

@router.post("/")
def create_expense(expense: ExpensePost):
    new_expense = add_expense(expense)
    return get_expense(new_expense)

@router.get("/", response_model=list[ExpenseGet])
def read_expenses():
    return get_expenses()


@router.get("/{expense_id}", response_model=ExpenseGet)
def read_expense_by_id(expense_id: int):
    return get_expense(expense_id)


@router.put("/{expense_id}")
def edit_expense(expense: ExpensePut):
    return update_expense(expense.expense_id)


@router.delete("/{expense_id}")
def delete_expense(expense_id: int):
    if remove_expense(expense_id):
        return {"message": "expense deleted succesfully"}
