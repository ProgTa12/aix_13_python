from urllib import request
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+%EC%84%9C%EC%9A%B8&ackey=q0y6o1bi"
target = request.urlopen(url) # 접속정보 등록
soup = BeautifulSoup(target, "html.parser")

tag = "div.temperature_text" # 온도
# 포함한 모든 글자
temp = soup.select_one(tag).get_text()
print('temp= ', temp)