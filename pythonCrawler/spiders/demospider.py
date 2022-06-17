import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


def get_urls(filename):
        f = open(filename).read().split()
        urls = []
        for i in f:
                urls.append("https://"+i)
        return urls 

class DemospiderSpider(CrawlSpider):
    name = 'demospider'
    def __init__(self, filename="pythonCrawler/spiders/million.txt"):
        super().__init__()
        self.start_urls = get_urls(filename)

    

    

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

