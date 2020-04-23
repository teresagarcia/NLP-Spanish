import scrapy


class CervantesSpider(scrapy.Spider):
    name = "cervantes_spider"
    start_urls = ['http://www.cervantesvirtual.com/obra-visor/el-ingenioso-hidalgo-don-quijote-de-la-mancha-6/html/']

    def parse(self, response):
        LINKS_SELECTOR = '.links'
        for chapter in response.css(LINKS_SELECTOR):
            URL_SELECTOR = 'a ::attr(href)'
            yield {
                'url': chapter.css(URL_SELECTOR).extract_first(),
            }

