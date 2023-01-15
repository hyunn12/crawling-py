import requests
from bs4 import BeautifulSoup

# naver 서버에 대화를 시도
response = requests.get("http://www.naver.com")

# naver에서 html 추출
html = response.text

# html.parser 를 통해 soup 생성
soup = BeautifulSoup(html, 'html.parser')

# id 값이 NM_set_home_btn 인 요소 추출
word = soup.select_one('#NM_set_home_btn')

# 해당 요소의 텍스트만 추출
print(word.text)
