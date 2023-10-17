# step1.프로젝트에 필요한 패키지 불러오기

from bs4 import BeautifulSoup as bs

import requests

# step2. 검색할 키워드 입력
# query = input('검색할 키워드를 입력하세요: ')

# step3. 입력받은 query가 포함된 url 주소(네이버 뉴스 검색 결과 페이지) 저장


volumeNum = 4
chapterNum = 1
erorChapter = 1
erorVol = 1


def getURL():
    url = f'http://royalroadweed.blogspot.com/2014/11/volume-{volumeNum}-chapter-{chapterNum}.html'

    return url


# step4. requests 패키지를 이용해 'url'의 html 문서 가져오기


def getHtmlText():
    response = requests.get(getURL())
    html_text = response.text

    return html_text


# step5. beautifulsoup 패키지로 파싱 후, 'soup' 변수에 저장
# 제목얻기
def getBody():
    textList = []
    soup = bs(getHtmlText(), 'html.parser')
    # div 요소를 찾고 class="post-entry inside" 조건을 만족하는 첫 번째 요소 선택
    div_element = soup.find('div', class_='post-entry inside')

    # 선택한 div 요소의 자식인 span 요소들 가져오기
    span_elements = div_element.find_all('div')

    for span in span_elements:
        textList.append(span.text)
    return textList

# 원하는 만큼 반복


# 파일을 얻는다.
def getText():
    try:
        # 파일 이름을 생성, i에 따라 파일 이름이 변경됨
        filename = f'sculptor/sculptor-{volumeNum}-{chapterNum}.txt'
        textList = getBody()

        # 파일을 쓰기 모드로 열고 텍스트를 파일에 쓰기
        with open(filename, 'w', encoding='utf-8') as file:
            for text in textList:
                file.write(text + '\n')  # 각 텍스트를 파일에 쓰고 개행 문자로 구분

    except Exception as e:
        # 파일 작업 중 예외가 발생하면 여기서 처리
        print(f'파일 작업 중 오류 발생: {volumeNum}-{chapterNum}')


firstChapterNum = 1
finalChapterNum = 15

if __name__ == "__main__":
    nextChapter = 1
    nextVom = 1
    chapterReset = 1
    for vomIndex in range(0, 25):
        chapterNum = chapterReset
        for index in range(firstChapterNum, finalChapterNum + 1):
            getText()
            chapterNum = chapterNum + nextChapter
        volumeNum = volumeNum + nextVom
