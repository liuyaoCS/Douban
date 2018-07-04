from lxml import etree
import requests

movie_url = "https://movie.douban.com/subject/4603382/"
content = requests.get(movie_url).text
html = etree.HTML(content)
#print(str(html))
info = html.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
print(info)