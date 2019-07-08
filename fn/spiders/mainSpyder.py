# -*- coding: utf-8 -*-
import scrapy


class MainspyderSpider(scrapy.Spider):
    name = 'mainSpyder'
    allowed_domains = ['finanznachrichten.de']
    start_urls = [
        'http://www.finanznachrichten.de/nachrichten-medien/archiv-dpa-afx-1.htm']

    def extractText(self, response):
        isin = []
        dateText = response.css('#DateTimeReaders::text').extract()
        #dateText = dateText.split()
        text = response.xpath(
            "//div[@id='artikelTextPuffer']/p//text()").extract()
        if "ISIN " in text[len(text)-2]:
            isin = text[len(text)-2].split()
            del isin[0]
        text = ''.join(str(x) for x in text)
        print(text)

    def parse_dir_contents(self, response):
        for quote in response.css('.hoverable  a::attr(href)').extract():
            url = response.urljoin(quote)
            yield scrapy.Request(url=url, callback=self.extractText)

    def parse(self, response):
        # yield from response.follow_all(response.css('.info .zentriert > a::attr(href)'), self.parse_sub)
        for next_page in response.css('.info .zentriert > a::attr(href)').extract():
            url = response.urljoin(next_page)
            yield scrapy.Request(url=url, callback=self.parse_dir_contents)
            # yield response.follow(next_page.root, self.parse_sub)
