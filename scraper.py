import scrapy


class BricketSetSpider(scrapy.Spider):
    name = "brickset_spider"

    def __init__(self, filename=None):
        if filename:
            with open(filename, 'r') as f:
                self.start_urls = f.readlines()