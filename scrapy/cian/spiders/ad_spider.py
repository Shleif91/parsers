import scrapy
import json


class AdSpider(scrapy.Spider):
    name = "ad"

    def start_requests(self):
        for i in range(1, 55):
            params = {"jsonQuery": {"region": {"type": "terms", "value": [2]}, "_type": "flatsale",
                                    "engine_version": {"type": "term", "value": 2},
                                    "building_status": {"type": "term", "value": 2},
                                    "page": {"type": "term", "value": i}}}

            yield scrapy.FormRequest('https://api.cian.ru/search-offers/v2/search-offers-desktop/',
                                     callback=self.parse,
                                     method='POST',
                                     body=json.dumps(params),
                                     headers={})

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())

        for offer in jsonresponse['data']['offersSerialized']:
            yield {
                'id': offer['id'],
                'title': offer['title'],
                'description': offer['description'],
                'jk': offer['geo']['jk']['displayName'],
                'floorNumber': offer['floorNumber'],
                'creationDate': offer['creationDate'],
                'price': offer['bargainTerms']['priceRur'],
                'totalArea': offer['totalArea'],
                'livingArea': offer['livingArea'],
                'offerType': offer['offerType'],
                'quarterEnd': offer['building']['deadline']['quarterEnd'],
                'materialType': offer['building']['materialType'],
                'floorsCount': offer['building']['floorsCount'],
                'flatType': offer['flatType'],
                'phone': offer['phones'][0]['number'],
                'photo': offer['photos'][0]['fullUrl'],
            }
