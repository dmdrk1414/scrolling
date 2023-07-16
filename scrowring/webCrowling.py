# step1.프로젝트에 필요한 패키지 불러오기

from bs4 import BeautifulSoup as bs

import requests

# step2. 검색할 키워드 입력
# query = input('검색할 키워드를 입력하세요: ')

# step3. 입력받은 query가 포함된 url 주소(네이버 뉴스 검색 결과 페이지) 저장

firstPage = 435
titleHtmlTag = 'h6'


def getURL(num):
    url = 'https://www.gwangju.go.kr/boardView.do?pageId=www788&boardId=BD_0000000022&seq=14' + \
        str(num) + '&movePage=1'
    return url

# step4. requests 패키지를 이용해 'url'의 html 문서 가져오기


def getHtmlText(urlNum):
    response = requests.get(getURL(urlNum))
    html_text = response.text
    return html_text


# step5. beautifulsoup 패키지로 파싱 후, 'soup' 변수에 저장
# 제목얻기
def getTitle(urlNum):
    soup = bs(getHtmlText(urlNum), 'html.parser')
    # title 태그 선택
    titleTag = soup.select(titleHtmlTag)

    # 마지막 </h6> 태그 제거
    titleStr = titleTag[0].text.strip('</h6>').strip()

    return titleStr

# 작성자 얻기


def getAuthor(urlNum):
    soup = bs(getHtmlText(urlNum), 'html.parser')

    authorSpan = soup.find('div', class_='board_view_info').find('span')
    authorStr = authorSpan.text.split(' : ')[1].strip()

    return authorStr

# 날짜 얻기


def getDate(urlNum):
    soup = bs(getHtmlText(urlNum), 'html.parser')

    dateSpan = soup.find('div', class_='board_view_info').findAll('span')
    dateStr = dateSpan[1].text.split(' : ')[1].strip()

    return dateStr

# 내용 얻기


def getContent(urlNum):
    soup = bs(getHtmlText(urlNum), 'html.parser')

    contentSpan = soup.find(class_='board_view_body')
    contentStr = contentSpan.text.strip()

    return contentStr


def getArticle(urlNum):
    title = getTitle(urlNum)
    author = getAuthor(urlNum)
    content = getContent(urlNum)
    date = getDate(urlNum)

    return [title, author, date, content]
