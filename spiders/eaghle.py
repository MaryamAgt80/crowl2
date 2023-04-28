import scrapy
from ..items import CrawlItem
class EaghleSpider(scrapy.Spider):
    name = 'eaghle'
    start_urls=[
        'https://www.parsnaz.com/%D9%87%D8%A7%D9%86%D8%AF%D9%87-%D8%A7%D8%B1%DA%86%D9%84.html',
        'https://musicguitars.ir/ebi-songs-colletion/'
    ]
    def parse(self, response):
        pictures=[]

        data=CrawlItem()
        for item in response.css('div.thumb'):

            url_don=response.urljoin(item.css('img ::attr(src)').get())
            pictures.append(url_don)
        data['image_urls']=pictures
        yield data
        files=[]
        for item in response.css('a.gmsdl'):
            url_don=item.css(' ::attr(href)').get()
            files.append(url_don)
        data['file_urls']=files
        yield data











