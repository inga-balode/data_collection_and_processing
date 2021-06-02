from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from lermerparser.spiders.lermer import LermerSpider
from lermerparser import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LermerSpider, search = 'стеллаж')

    process.start()