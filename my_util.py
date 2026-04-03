from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

# 도시 이름 입력
def get_weather(city="서울"):
    city = quote_plus(city)

    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%9D%BC%EA%B8%B0%EC%98%88%EB%B3%B4+"+city
    target = request.urlopen(url) # 접속정보 등록
    soup = BeautifulSoup(target, "html.parser")

    tag = "div.temperature_text" # 온도
    mytemp = soup.select_one(tag).get_text().strip() # 공백이 많음
    
    # 포함한 모든 글자
    tag = "div.temperature_info" # 습도, 날씨, 풍량
    temp = soup.select_one(tag).get_text() # 공백이 많음
    temp = temp.strip() # 앞 뒤 공백제거
    temp = ' '.join(temp.split()) # 모든 공백을 1개 공백으로 압축 
    temp = temp.split()
    return { 
            'temp' : mytemp,
            'yestd': temp[1] + " " + temp[2],   # 어제보다 0도 높아요
            'weather': temp[3],                 # 날씨
            'hum': temp[7],                     # 습도
            'windd': temp[8],                   # 풍향
            'windsp': temp[9]                   # 풍속
            }     
    
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


if __name__ == "__main__":
    city = "수원"
    ans = get_weather(city)
    print(f'{city}온도는 {ans['temp']}')
    ans = get_dust(city)
    print(f"{city} 미세먼지 농도는 {ans['오전']}")