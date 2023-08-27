제가 웹 크롤링을 처음 해봐서ㅠ 참힘들었네요🤣



1. 구글 드라이버 설치 (크롬 버전과 동일) : 

   https://chromedriver.chromium.org/downloads

   - 크롬 현제 : 버전 114.0.5735.198(공식 빌드) (arm64)
   - 크롬 드라이버 버전 : **[ChromeDriver 114.0.5735.90](https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/)**
   - 주의 : 크롬 버전과 드라이버 버전은 동일해야한다.



# ✅ webcrolling 을 하기위한 환경 

IDE : Visual Studio Code

언어 : python : 3.11.3

container : Docker version 24.0.2, build cb74dfc

Database : mysql : 8.0.33 (databas 이름 : second_sessions )

Rest API : FastAPI : 0.100.0

구글 드라이버 설치

- https://chromedriver.chromium.org/downloads
- 크롬 현제 : 버전 114.0.5735.198(공식 빌드) (arm64)
- 크롬 드라이버 버전 : **[ChromeDriver 114.0.5735.90](https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/)**
- 주의 : 크롬 버전과 드라이버 버전은 동일해야한다.

## ✅ 각 환경별 라이브러리 확인

이렇게 크게 4개의 환경을 설정하고용

## python

1. anaConda : conda 23.5.1
   - 파이썬 편한 환경설정을 위한 것

2. BeautifulSoup 4.12.2 
   - 크롤링을 하기위한 라이브러리

## Mysql

1. Pymysql 1.1.0 
   - python에서 DB을 연결을 하기위한 라이브러리



# ✅ 크롤링 기본 함수 (난잡합니다.)

https://wikidocs.net/135794

```
 # requests 패키지 가져오기
 import requests
 
 # BeautifulSoup 패키지 불러오기
 # 주로 bs로 이름을 간단히 만들어서 사용함
 from bs4 import BeautifulSoup as bs
 
 # 가져올 url 문자열로 입력
 url = 'https://www.naver.com'
 
 # requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
 response = requests.get(url)
 
 # 우리가 얻고자 하는 html 문서가 여기에 담기게 됨
 html_text = response.text
 
 # html을 잘 정리된 형태로 변환
 html = bs(html_text, 'html.parser')
 
 print(html_text)
```

```
 # 목표 태그 예)
 <p class = "para">코딩유치원</p>
 <div id = "zara">코딩유치원</p>
 
 # 태그 이름으로 찾기
 soup.find('p')
 
 # 태그 속성(class)으로 찾기 - 2가지 형식
 soup.find(class_='para') #이 형식을 사용할 때는 class 다음에 언더바_를 꼭 붙여주어야 한다
 soup.find(attrs = {'class':'para'})
 
 # 태그 속성(id)으로 찾기 - 2가지 형식
 soup.find(id='zara')
 soup.find(attrs = {'id':'zara'})
 
 # 태그 이름과 속성으로 찾기
 soup.find('p', class_='para')
 soup.find('div', {'id' = 'zara'})
 
 
```

# ✅ Fast api - conda 이용 설치

```
# base 환경 활성화
conda activate base

# FastAPI 설치 (Conda 사용)
conda install fastapi

# 또는 pip를 사용하여 FastAPI 설치
pip install fastapi

# Uvicorn 설치 (Conda 사용)
conda install uvicorn

# 또는 pip를 사용하여 Uvicorn 설치
pip install uvicorn

# 파일 저장시 서버를 자동으로 다시 시작합니다.
# 서버는 http://localhost:8000 에서 접근 가능합니다.
uvicorn main:app --reload

```



# ✅ docker 및 mysql 환경설정

mariadb 도커 컨테이너 실행 : https://malwareanalysis.tistory.com/140

도커 설치 : https://docs.docker.com/desktop/install/mac-install/

```
 # docker hub을 이용해 push 하기

 #docker commit을 통해 python 을 설치한 my-python 실행 컨테이너를 이미지화 한다.
 #my-python 컨테이너를 didwlsdbs/python3 이름으로 이미지로 만든다. (태그 : 1.0)
 docker commit my-python didwlsdbs/python3:1.0
 
 #이미지가 생성되었는지 확인
 docker images
 
 #docker 허브로 로그인한다
 dockert login
 
 #화면에 도커허브의 계정을 입력하는 화면이 나오고 계정을 입력하면 된다.
 #docker 허브 화면에 표시되었던 push 명령어를 참고해서 push한다.
 docker push didwlsdbs/python3:1.0
 
 #docker 허브 사이트에 해당 이미지가 올라감을 확인할 수 있고,
 #세팅했던 이미지를 삭제후 도커허브의 이미지를 다운받아보자.
 docker rmi --force didwlsdbs/python3:1.0
 docker pull didwlsdbs/python3:1.0


# 컨테이너 목록 출력
docker ps -a 

# MySQL Docker 컨테이너 중지
$ docker stop mysql-container

# MySQL Docker 컨테이너 시작
$ docker start mysql-container

# MySQL Docker 컨테이너 재시작
$ docker restart mysql-container

# mySQL 컨테이너 bash 쉘 접속
docker exec -it "컨테이너 이름" bash


#----------------
도커시작

# 도커 안에서 mysql 을 실행하는 방법
mysql -u root -p
```

# ✅ docker안의 mysql 과 로컬의 mysql 연결하는 방법

```java
1. 도커 설치하고 명령어 창에 등록
docker run -d -p 3306:3306 --name restAPI-DB-container -e MYSQL_DATABASE=scrollingDB -e MYSQL_USER=dmdrk1414 -e MYSQL_PASSWORD=qkrtmdcks1! -e MYSQL_ROOT_PASSWORD=qkrtmdcks1! mysql:latest

/*
run -d \    # 시작
> -p 3306:3306 \  # 포트포워딩 외부접속, 도커 컨테이너 포트
> --name restAPI-DB-container \  # 컨테이어 이름
> -e MYSQL_DATABASE=scrollingDB \  # 데이터베이스 이름 (시작과 동시에 생성)
> -e MYSQL_USER=dmdrk1414 \ # 일반 계정 생성
> -e MYSQL_PASSWORD=qkrtmdcks1! \ # 일반 계정 비번
> -e MYSQL_ROOT_PASSWORD=qkrtmdcks1! \ # root 계정 비번
mysql:latest  # 버전
*/
  
2. brew을 이용해 mysql 설치 
https://velog.io/@haleyjun/MySQL-Mac%EC%97%90-MySQL-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-M1%EC%B9%A9

# docker의 mysql의 port 확인하기
# mysql:latest
# 0a94d6cff443
# 3306:3306

# local mysql으로 접속 homebrew으로 mysql 설치한 결과
# local mysql과 docker의 mysql 사용하는 방법
cd /opt/homebrew/opt/mysql@8.0/bin 
  
./mysql -h 127.0.0.01 -P 3306 -u root -p
```



### SQL 문법

```sql
SELECT * FROM oldmanDisablesTable;
ALTER TABLE oldmanDisablesTable AUTO_INCREMENT = 1;
DELETE FROM oldmanDisablesTable;
http://localhost:8000/oldmanDisablesTable

SELECT * FROM recipientsTable;
ALTER TABLE recipientsTable AUTO_INCREMENT = 1;
DELETE FROM recipientsTable;
http://localhost:8000/recipientsTable

SELECT * FROM pregnantsTable;
ALTER TABLE pregnantsTable AUTO_INCREMENT = 1;
DELETE FROM pregnantsTable;
http://localhost:8000/pregnantsTable
```



