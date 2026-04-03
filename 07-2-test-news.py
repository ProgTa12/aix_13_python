from urllib import request
from bs4 import BeautifulSoup

url = "https://news.naver.com/section/105"
target = request.urlopen(url) # 접속정보 등록
soup = BeautifulSoup(target, "html.parser")

tag = "li.rl_item .rl_txt"
temp = soup.select(tag)

for t in temp:
    title = t.get_text()
    print('기사 제목', title)

print("end")