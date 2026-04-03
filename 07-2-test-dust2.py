from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def get_dust(city = "서울"):
    city = quote_plus(city)
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+"+city
    target = request.urlopen(url) # 접속정보 등록
    soup = BeautifulSoup(target, "html.parser")

    # 미세먼지 오전
    tag = "div.detail_info.lv3 > dl" # 습도, 날씨, 풍량
    temp = soup.select_one(tag).get_text()
    temp = ' '.join(temp.split())
    temp = temp.split()
    result = {temp[0] : temp[1]}

    # 미세먼지 오후
    tag = "div.detail_info.lv2 > dl" # 습도, 날씨, 풍량
    temp = soup.select_one(tag).get_text()
    temp = ' '.join(temp.split())
    temp = temp.split()
    result[temp[0]] = temp[1]
    # print('result' , result)
    return result

soup = get_dust()


# temp = soup.select("dd.lvl") # 여러개
# print(list(temp))  