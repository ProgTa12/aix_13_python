from urllib import request
from bs4 import BeautifulSoup


def countries_money():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=ghksdbf&ackey=q6yiz04y"
    target = request.urlopen(url) # 접속정보 등록
    soup = BeautifulSoup(target, "html.parser")

    tag = ".nt_slc._select"
    countries = soup.select(".nt_slc._select option")

    print("--- 국가 목록 추출 ---")
    for opt in countries:
        country_name = opt.get_text().strip()
        print(f"국가명: {country_name}")

    tag = ".api_subject_bx .inner .num .recite"
    money = soup.select(tag)
    usd = money[0].get_text().strip()
    krw = money[1].get_text().strip()

    return country_name,usd,krw
country_name, usd , krw = countries_money()

country_name, usd, krw = countries_money()
print(f"미국의 환율은 {usd} = {krw}")

print("end")