from urllib import request
from bs4 import BeautifulSoup

def get_currency_dict():
    url = "https://finance.naver.com/marketindex/exchangeList.naver"
    target = request.urlopen(url)
    soup = BeautifulSoup(target, "html.parser")

    country_tags = soup.select(".tbl_area .tit")
    money_tags = soup.select(".tbl_area .sale")
    return {c.get_text().strip(): m.get_text().strip() for c, m in zip(country_tags, money_tags)}

exchange_data = get_currency_dict()

user_input = input("국가명 입력: ").strip()

for country, rate in exchange_data.items():
    if user_input in country:
        print(f"{country}: {rate}")
