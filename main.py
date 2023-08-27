from typing import Optional

from fastapi import FastAPI
from app.database.utill import createArticle, delete_article
from scrowring.webCrowling import getArticle

import time
import json
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
    tempList = []
    id = 0
    for num in range(firstPage, firstPage + 30):
        article = getArticle(num)
        title = article[TITLE]
        author = article[AUTHOR]
        date = article[DATE]
        content = article[CONTENT]

        print(title)
        print(author)
        print(date)
        print(content)

        tempList.append({
            'id': id,
            'title': title,
            'author': author,
            'date': date,
            'content': content,
            'isScrapCheck': False
        })
        id = id + 1
        # 비동기 함수 호출
        # await createArticle(oldmanDisablesTable, title, author, date, content)
    with open("oldmanDisablesTable.json", "w", encoding="utf-8") as json_file:
        json.dump(tempList, json_file, ensure_ascii=False)

    return {"Hello": "World"}


@app.get("/recipientsTable")
async def read_root():
    tempList = []
    id = 0
    for num in range(firstPage + 30, firstPage + 55):
        article = getArticle(num)
        title = article[TITLE]
        author = article[AUTHOR]
        date = article[DATE]
        content = article[CONTENT]

        tempList.append({
            'id': id,
            'title': title,
            'author': author,
            'date': date,
            'content': content,
            'isScrapCheck': False
        })
        id = id + 1

        # 비동기 함수 호출
        # await createArticle(recipientsTable, title, author, date, content)
    with open("recipientsTable.json", "w", encoding="utf-8") as json_file:
        json.dump(tempList, json_file, ensure_ascii=False)
    return {"Hello": "World"}


@app.get("/pregnantsTable")
async def read_root():
    tempList = []
    id = 0
    for num in range(firstPage + 60, firstPage + 90):
        article = getArticle(num)
        title = article[TITLE]
        author = article[AUTHOR]
        date = article[DATE]
        content = article[CONTENT]

        tempList.append({
            'id': id,
            'title': title,
            'author': author,
            'date': date,
            'content': content,
            'isScrapCheck': False
        })
        id = id + 1
        # 비동기 함수 호출
        # await createArticle('pregnantsTable', title, author, date, content)
    with open("pregnantsTable.json", "w", encoding="utf-8") as json_file:
        json.dump(tempList, json_file, ensure_ascii=False)
    return {"Hello": "World"}


# SELECT * FROM oldmanDisablesTable;
# http://localhost:8000/oldmanDisablesTable

# SELECT * FROM recipientsTable;
# http://localhost:8000/recipientsTable

# SELECT * FROM pregnantsTable;
# http://localhost:8000/pregnantsTable
