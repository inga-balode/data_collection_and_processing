import scrapy
from scrapy.http import HtmlResponse
from lermerparser.items import LermerItem
from scrapy.loader import ItemLoader

class LermerSpider(scrapy.Spider):
    name = 'lermer'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        super(LermerSpider, self).__init__()
        self.start_urls = [f'https://leroymerlin.ru/search/?q={search}']

    def parse(self, response: HtmlResponse):
        goods_links = response.xpath("//a[@data-qa = 'product-name']/@href").extract()
        for link in goods_links:
            yield response.follow(link, callback=self.parse_good)

        next_page = response.xpath("//a[contains(@aria-label, 'Следующая страница')]/@href").extract()
        yield response.follow(next_page, callback=self.parse_good)

    def parse_good(self, response: HtmlResponse):
        loader = ItemLoader(item=LermerItem(), response=response)

        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('photos', "//img[@alt = 'image thumb']/@src")
        loader.add_xpath('specs_all', "//dt/text()")
        loader.add_xpath('specs', "//dd/text()")
        loader.add_xpath('price', "//span[@slot = 'price']/text()")
        loader.add_value('link', response.url)

        yield loader.load_item()
