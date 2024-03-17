import requests
from bs4 import BeautifulSoup

def crawl_naver_map(url):
    # HTTP GET 요청 보내기
    response = requests.get(url)
    
    # 요청에 성공했을 때
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 카페 정보 추출
        cafes = soup.select('._2aX_A')
        
        # 결과 출력
        print("카페 정보:")
        for cafe in cafes:
            name = cafe.select_one('.aXvQv').text.strip()
            address = cafe.select_one('._3LMxZ').text.strip()
            print(f"이름: {name}, 주소: {address}")
    else:
        print("네이버 지도에서 정보를 가져오지 못했습니다.")

# 지정된 URL에서 카페 정보 크롤링
crawl_naver_map("https://map.naver.com/p/search/%EC%B9%B4%ED%8E%98?c=12.51,0,0,0,dh")
