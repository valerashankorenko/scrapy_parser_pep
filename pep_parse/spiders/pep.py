import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Метод для сбора ссылок на документы PEP."""
        pep = response.css('td')
        for link in pep:
            href = link.css('a::attr(href)').get()
            if href is not None:
                if not href.endswith('/'):
                    href += '/'
                yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response):
        """Метод для парсинга страницы документа PEP."""
        name = response.css('h1.page-title::text').get()
        number = name.split()[1]
        status = response.css('abbr::text').get()
        if status is not None:
            data = {
                'number': number,
                'name': name,
                'status': status,
            }
            yield PepParseItem(data)
