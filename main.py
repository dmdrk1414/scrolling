from typing import Optional

from fastapi import FastAPI
from app.database.utill import createArticle, delete_article
from scrowring.webCrowling import getArticle

import time

app = FastAPI()

TITLE = 0
AUTHOR = 1
DATE = 2
CONTENT = 3
firstPage = 300
oldmanDisablesTable = 'oldmanDisablesTable'
recipientsTable = 'recipientsTable'
pregnantsTable = 'pregnantsTable'


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/oldmanDisablesTable")
async def read_root():
    for num in range(firstPage, firstPage + 30):
        article = getArticle(num)  # 비동기 함수 호출
        title = article[TITLE]
        author = article[AUTHOR]
        date = article[DATE]
        content = article[CONTENT]

        print(article)

        # 비동기 함수 호출
        await createArticle('oldmanDisablesTable', title, author, date, content)

    return {"Hello": "World"}


@app.get("/recipientsTable")
async def read_root():
    for num in range(firstPage + 30, firstPage + 60):
        article = getArticle(num)  # 비동기 함수 호출
        title = article[TITLE]
        author = article[AUTHOR]
        date = article[DATE]
        content = article[CONTENT]

        print(article)

        # 비동기 함수 호출
        await createArticle(recipientsTable, title, author, date, content)
    return {"Hello": "World"}


@app.get("/pregnantsTable")
async def read_root():
    for num in range(firstPage + 60, firstPage + 30):
        article = getArticle(num)  # 비동기 함수 호출
        title = article[TITLE]
        author = article[AUTHOR]
        date = article[DATE]
        content = article[CONTENT]

        print(article)

        # 비동기 함수 호출
        await createArticle(pregnantsTable, title, author, date, content)
    return {"Hello": "World"}


# SELECT * FROM oldmanDisablesTable;
# http://localhost:8000/oldmanDisablesTable

# SELECT * FROM recipientsTable;
# http://localhost:8000/recipientsTable

# SELECT * FROM pregnantsTable;
# http://localhost:8000/pregnantsTable
