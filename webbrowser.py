import webbrowser
import time
from urllib.parse import quote

QIYI_BASE_URL='http://so.iqiyi.com/so/q_{}?'
movies = open('test.txt')
for movie in movies:
    movie = quote(movie, 'utf-8')
    webbrowser.open(QIYI_BASE_URL.format(movie))
    time.sleep(1)
movies.close()
