import sys

import pymysql
from setuptools import logging

import string
import re

import requests
from bs4 import BeautifulSoup

# 연결정보
host = "localhost"
port = "3306"
database = "brewery"
username = "test"
password = "test"


def main():

    try:
        # DB Connection 생성
        conn = pymysql.connect(host=host, user=username, passwd=password, db=database, use_unicode=True, charset='utf8')
        cursor = conn.cursor()

    except:
        logging.error("")
        sys.exit(1)

    for i in range(1, 27, 1):
        print('========================================================================================')
        url = f'http://www.kajawine.kr/shop/list.php?ca_id=20&sort=it_type4&sortodr=desc&type_color=&it_price=&it_opt4=&it_opt9=&page={i}'
        response = requests.get(url)

        html = response.text

        soup = BeautifulSoup(html, 'html.parser')

        links = soup.select('.item_thumb')

        for link in links:
            imgTag = link.select_one('.listImg > a > img')
            # 이름
            name = re.split(r'[\[\]{}():]+', imgTag.attrs['alt'])[0]
            print(name)

            # 이미지
            path = imgTag.attrs['src']
            print(path)

            print('--------------------------------------')

            attribute = link.select_one('.list_ex')
            text = attribute.text

            # 도수
            volume = text.split('알콜도수 : ')[1].split('%')[0]
            print(volume)

            # 용량
            capacity = text.split('용량 : ')[1].split('알콜도수')[0].split('ml')[0]
            print(capacity)

            # 종류 -> ???
            print(text.split('종류 : ')[1].split('용량')[0])

            print('--------------------------------------')

            query = "insert into TBL_WHISKEY(name, volume, capacity, `desc`, image_path) VALUES (%s, %s, %s, '테스트양주', %s);"
            value = (name, volume, capacity, path)
            print(query)
            print(value)

            cursor.execute(query, value)
            print('========================================================================================')

    conn.commit()

    conn.close()

if __name__ == '__main__':
    main()