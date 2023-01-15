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
        attribute = link.select_one('.list_ex')
        print(attribute.text)
        print('--------------------------------------')
        name = link.select_one('.listImg > a > img')
        print(name.attrs['alt'])
        print('--------------------------------------')

    print('========================================================================================')
