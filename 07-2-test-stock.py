from urllib import request
from bs4 import BeautifulSoup

def get_stock():
    url = "https://search.naver.com/search.naver?where=nv&sm=top_sug.ansstk&fbm=0&acr=1&acq=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&qdt=0&ie=utf8&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90+%EC%A3%BC%EA%B0%80&ackey=bicymdjr"
    target = request.urlopen(url) # 접속정보 등록
    soup = BeautifulSoup(target, "html.parser")

    tag = ".spt_tlt .stk_nm"
    company = soup.select_one(tag).get_text().strip()
    
    tag = ".stock_quote .spt_con strong"
    # tag = "a.target"
    # 포함한 모든 글자
    temp = soup.select_one(tag).get_text()
    return company, temp

company, stock = get_stock()
print(f"현재 {company}의 주가는: {stock}")