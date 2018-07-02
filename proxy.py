import requests

def requests_proxy(url):

    proxy = {
        'http': 'http://187.12.44.34:8080',
        'https': 'https://187.12.44.34:8080'
    }

    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Connection': 'keep-alive'
    }

    request = requests.get('https://book.douban.com/top250?start=0', headers=head, proxies=proxy)
    return request

