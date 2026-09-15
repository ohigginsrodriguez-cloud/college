from pydantic import BaseModel, Field
from datetime import date


class expense(BaseModel):
    name: str
    amount: float
    description: str | None
    category: str
    date: date
