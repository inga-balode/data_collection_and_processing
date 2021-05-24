from lxml import html
from pprint import pprint
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

response = requests.get('https://lenta.ru/')
dom = html.fromstring(response.text)

all_news =[]

items = dom.xpath("//div[@class = 'span4']/div[@class = 'item' or @class = 'first-item']")
for item in items:
    news ={}
    news['time'] = item.xpath(".//time[@class = 'g-time']/text()")
    news['date'] = item.xpath(".//time/@title")
    news_l = item.xpath(".//a/@href")
    news['link'] = f'https://lenta.ru{news_l[0]}'
    news['news'] = item.xpath(".//a[contains (@href, '/news/')]/text()")
    news['resource'] = "lenta.ru"
    all_news.append(news)

pprint(all_news)

