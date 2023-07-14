import pymysql


def createArticle(database, title, author, date, content):
    # db 연결
    db = pymysql.connect(host="localhost", user="root",
                         passwd="qkrtmdcks1!", charset="utf8")

    # MySQL 커서 생성
    cursor = db.cursor()

    # 데이터 베이스 선택
    cursor.execute("USE second_sessions")

    # INSERT 문 실행
    sql = "INSERT INTO " + \
        str(database) + " (title, author, date, content) VALUES (%s, %s, %s, %s)"
    values = (title, author, date, content)
    cursor.execute(sql, values)

    # 변경사항 커밋
    db.commit()

    # 연결 종료
    cursor.close()
    db.close()


def delete_article(database):
    # db연결
    db = pymysql.connect(host="localhost", user="root",
                         passwd="qkrtmdcks1!", charset="utf8")

    # MySQL 커서 생성
    cursor = db.cursor()

    # 데이터 베이스 선택
    cursor.execute("USE second_sessions")

    # DELETE 문 실행
    sql = "DELETE FROM " + str(database)
    cursor.execute(sql)

    # 변경사항 커밋
    db.commit()

    # 연결 종료
    cursor.close()
    db.close()
