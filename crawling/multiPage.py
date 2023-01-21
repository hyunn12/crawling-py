import requests
from bs4 import BeautifulSoup

# 반복문 통해 여러 페이지 조회
for i in range(1, 27, 1):
    print('========================================================================================')
    print(i)

    url = f'http://www.kajawine.kr/shop/list.php?ca_id=20&sort=it_type4&sortodr=desc&type_color=&it_price=&it_opt4=&it_opt9=&page={i}'
    print(url)
    response = requests.get(url)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    links = soup.select('.item_thumb')

    for link in links:
        # select_one 이 아닌 select 로 조회 시 배열로 조회되어 .text 속성을 사용할 수 없기 때문에 주의!
        # ERROR: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
        attribute = link.select_one('.list_ex')
        print(attribute.text)
        print('--------------------------------------')
        name = link.select_one('.listImg > a > img')
        print(name.attrs['alt'])
        print('--------------------------------------')

    print('========================================================================================')



# 고민할 점
# 현재 선택한 사이트의 경우 상세 용량이나 도수 등을 목록에서 바로 가져올 수 있지만 포맷이 애매..
#       ex) 종류 : 용량 : 700ml 알콜도수 : 40%	| 맥켈란 퀘스트
#  하나의 태그에 하나의 정보만 있지 않아 덩어리로 정보가 가져와짐

# 1. 일단 가져와서 쿼리단에서 분리해 집어넣을 수 있을까?
# 2. 혹은 일단 가져온 후 나중에 데이터 클리닝?
# 3. 이미지의 경우 어떻게 처리할 것인지?

# 4. 현재는 가져와서 그냥 콘솔에 프린트하지만 DB에 저장하는 로직도 필요함