#!/usr/local/bin/python3
from lxml import etree
import requests
import time
import re

def requests_proxy(url):

    proxy = {
        'http': 'http://187.12.44.34:8080',
        'https': 'https://187.12.44.34:8080'
    }

    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Connection': 'keep-alive'
    }

    request = requests.get(url, headers=head, proxies=proxy)
    return request


def filter_inner(movie_url):
    data = requests_proxy(movie_url).text
    s = etree.HTML(data)
    info = s.xpath('//*[@id="info"]/text()')
    for i in range(len(info)):
        info_item = s.xpath('//*[@id="info"]/span[{}]/text()'.format(i))
        str_item = str(info_item)
        search_obj = re.search(r'动画|短片|纪录片|音乐|运动|脱口秀|舞台|歌舞', str_item)
        if search_obj:
            return 0
        elif str_item.find("上映日期") >= 0:
            pub_date = s.xpath('//*[@id="info"]/span[{}]/text()'.format(i+1))
            year = str(pub_date)[2:6]
            if int(year) < 1990:
                return 0
    return 1


# genres=剧情 喜剧 动作 爱情 科幻 悬疑 惊悚 恐怖 犯罪 战争 西部 奇幻 冒险 灾难 情色
URL = 'https://movie.douban.com/j/new_search_subjects?sort=T&range={}&tags=电影&genres={}&countries=美国&start={}'
LIMIT = 100
count = 0

with open('/Users/liuyao/home/project/python/douban/movie.csv','w') as f:
    for pid in range(LIMIT):
        url_visit = URL.format("9,10", "恐怖", pid * 20)
        file = requests_proxy(url_visit).json()

        if len(file['data']) == 0:
            print("search "+str(count)+" movies over!")
            break

        print("######## page id: "+str(pid)+" ########")
        for item in file['data']:
            url = item['url']
            title = item['title']
            rate = item['rate']
            casts = item['casts']

            ret = filter_inner(url)
            time.sleep(0.2)
            if ret == 1:
                print(' {}  {}  {}  {}\n'.format(title, rate, '  '.join(casts), url))
                #f.write(' {}  {}  {}  {}\n'.format(title, rate, '  '.join(casts), url))
                f.write("{},{},{},{}\n".format(title, rate, '  '.join(casts), url))
                count = count+1

        time.sleep(2)



