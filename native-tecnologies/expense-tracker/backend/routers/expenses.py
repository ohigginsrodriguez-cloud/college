from fastapi import APIRouter, HTTPException
from crud import add_expense, get_expenses, get_expense, update_expense, remove_expense
from models import ExpensePost, ExpenseGet


router = APIRouter(
        prefix="/expenses",
        tags=["expenses"],
        responses={404: {"description": "Not found"}},
        )

@router.post("/", response_model=ExpenseGet, status_code=201)
def create_expense(expense: ExpensePost):
    new_id = add_expense(expense)
    return get_expense(new_id)

@router.get("/", response_model=list[ExpenseGet])
def read_expenses():
    return get_expenses()


@router.get("/{expense_id}", response_model=ExpenseGet)
def read_expense_by_id(expense_id: int):
    expense = get_expense(expense_id) 
    if not expense: 
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


@router.put("/{expense_id}", response_model=ExpenseGet)
def edit_expense(expense_id: int, expense: ExpensePost):
    expense_updated = update_expense(expense_id, expense)
    if not expense_updated:
        raise HTTPException(status_code=404, detail="Expense not found")
    return get_expense(expense_id)

@router.delete("/{expense_id}")
def delete_expense(expense_id: int):
    expense = remove_expense(expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "expense deleted succesfully"}
