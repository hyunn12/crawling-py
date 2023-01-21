import sys

import pymysql
from setuptools import logging

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

    query = "insert into TBL_WHISKEY(whiskey_id, name, volume, capacity, `desc`, image_path) VALUES (1, 'test', 15, 500, '테스트양주', '')"

    cursor.execute(query)

    conn.commit()

    conn.close()

if __name__ == '__main__':
    main()