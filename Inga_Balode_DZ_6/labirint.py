import scrapy
from scrapy.http import HtmlResponse
from bookparser.items import LabirintItem


class LabirintSpider(scrapy.Spider):
    name = 'labirint'
    allowed_domains = ['labirint.ru']
    start_urls = ['https://www.labirint.ru/search/%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5/?stype=0']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@title = 'Следующая']/@href").extract_first()
        yield response.follow(next_page, callback=self.parse)

        books_links = response.xpath("//a[@class = 'product-title-link']/@href").extract()
        for link in books_links:
            yield response.follow(link, callback= self.book_parse)

    def book_parse(self, response: HtmlResponse):
        link = response.url
        name = response.xpath("//h1/text()").extract_first()
        author = response.xpath("//a[@data-event-label = 'author']/text()").extract_first()
        publisher = response.xpath("//a[@data-event-label = 'publisher']/text()").extract_first()
        new_price = response.xpath("//span[@class = 'buying-pricenew-val-number']/text()").extract_first()
        old_price = response.xpath("//span[@class = 'buying-priceold-val-number']/text()").extract_first()
        rate = response.xpath("//div[@id = 'rate']/text()").extract_first()
        item = LabirintItem(name=name, author=author, publisher= publisher, new_price = new_price, old_price = old_price, link = link, rate = rate)
        yield item