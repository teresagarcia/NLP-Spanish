import scrapy


class CervantesSpider(scrapy.Spider):
    name = "cervantes_spider"
    start_urls = ['http://www.cervantesvirtual.com/obra-visor/el-ingenioso-hidalgo-don-quijote-de-la-mancha-6/html/']

    def extract_text(self, response):
        URL_SELECTOR = 'string(//div[contains(@id,"obra")]/p)'
        yield{
            'text': response.selector.xpath(URL_SELECTOR).get()
        }

    def parse(self, response):
        found_chapters = []
        LINKS_SELECTOR = '.links'
        for chapter in response.css(LINKS_SELECTOR):
            URL_SELECTOR = 'a ::attr(href)'
            found_chapters.append(chapter.css(URL_SELECTOR).extract_first())
        
        for chapter in found_chapters:
            yield scrapy.Request(
                response.urljoin(chapter),
                callback=self.extract_text)
    
