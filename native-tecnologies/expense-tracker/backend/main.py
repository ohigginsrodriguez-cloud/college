from fastapi import FastAPI

from routers import expenses


app = FastAPI()


app.include_router(expenses.router)

@app.get("/")
def root():
    return {"message": "running..."}



