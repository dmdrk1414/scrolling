from typing import Optional

from fastapi import FastAPI
from app.database.utill import createArticle, delete_article


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/oldmanDisablesTable")
def read_root():
    createArticle('oldmanDisablesTable', 'Sample Title', 'Sample Target',
                  'Sample Period', 'Sample Content')
    return {"Hello": "World"}


@app.get("/recipientsTable")
def read_root():
    createArticle('recipientsTable', 'Sample Title', 'Sample Target',
                  'Sample Period', 'Sample Content')
    return {"Hello": "World"}


@app.get("/pregnantsTable")
def read_root():
    createArticle('pregnantsTable', 'Sample Title', 'Sample Target',
                  'Sample Period', 'Sample Content')
    return {"Hello": "World"}


# SELECT * FROM oldmanDisablesTable;
# http://localhost:8000/oldmanDisablesTable

# SELECT * FROM recipientsTable;
# http://localhost:8000/recipientsTable

# SELECT * FROM pregnantsTable;
# http://localhost:8000/pregnantsTable
