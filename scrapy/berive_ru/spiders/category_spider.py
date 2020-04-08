import scrapy


class QuotesSpider(scrapy.Spider):
    name = "category"
    start_urls = [
        'https://berive.ru/velosipedy/page-4/',
    ]

    def parse(self, response):
        for href in response.xpath('//div[@class="ty-grid-list__image"]//a/@href'):
            yield response.follow(href, self.parse_page)

        for a in response.xpath('//a[contains(@class,"ty-pagination__next")]/@href'):
            yield response.follow(a, callback=self.parse)

    def parse_page(self, response):
        params = {
            'title': response.xpath(
                '//div[@class="ty-product-block__left"]//h1[@class="ty-product-block-title"]/text()').get(),
            'recommend_price': response.xpath(
                '//div[@class="ty-product-block__left"]//span[contains(@class,"ty-list-price")]/text()').get(),
            'price': response.xpath(
                '//div[@class="ty-product-block__left"]//span[contains(@class,"ty-price-num")]/text()').get(),
        }

        for quote in response.xpath('//div[@class="n-product-spec-wrap__body"]//dl'):
            params[quote.xpath('dt/span/text()').get()] = quote.xpath('dd/span/text()').get()

        yield params