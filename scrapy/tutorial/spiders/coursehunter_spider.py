import scrapy


BASE_URL = 'https://coursehunter.net'
EMAIL = ''
PASSWORD = ''

class CoursehunterSpider(scrapy.Spider):
    name = "coursehunter"
    start_urls = [
        BASE_URL + '/sign-in',
    ]

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//form[@class="auth"]',
            formdata={
                'e_mail': EMAIL,
                'password': PASSWORD,
            },
            callback=self.after_login
        )

    def after_login(self, response):
        yield response.follow(BASE_URL + '/frontend/typescript', self.parse_category)


    def parse_category(self, response):
        for href in response.xpath('//div[@class="course-details-bottom"]/a/@href'):
            yield response.follow(href, self.parse_page)

        for href in response.xpath('//a[@rel="next"]/@href'):
            yield response.follow(href, self.parse_category)

    def parse_page(self, response):
        yield {
            'title': response.xpath('//h1[@class="hero-title"]/text()').get(),
            'source': response.xpath('//div[@class="hero-source"]/text()').get(),
            'link': response.xpath('//li[@class="lessons-item"]/link[@itemprop="url"]/@href').get(),
            'archive': response.xpath('//a[contains(@class, "section-block-btn") and contains(@class, "btn-outline")]/@href').getall(),
        }
