import scrapy
from terrorscrapper.items import TerrorItem
from terrorscrapper.SaveFile import SaveFile

class TerrorSpider(scrapy.Spider):
    name = 'terrorspider'
    allowed_domains = ['rewardsforjustice.net']
    start_urls = ['http://rewardsforjustice.net/rewards/']

    custom_settings = {
        'FEEDS':{
            SaveFile.json_file() : {'format' : 'json'},
            # SaveFile.xlsx_file() : {'format' : 'xlsx', 'encoding' : 'utf-8'},
            }
            # 'FEED_EXPORT_ENCODING' : 'utf-8'
    }

    def parse(self, response):
        # terrors = response.css('div.page-content')
        terrors = response.css('article.post')
        for terror in terrors:            
            terror_url = terror.css('h2.entry-title a::attr(href)').get()

            yield response.follow(terror_url, callback = self.parse_terror_page)

        # Extracting URL for next page
        next_page = response.css('div.nav-previous a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_terror_page(self, response):
        terror_item = TerrorItem()
        
        terror_item['url'] = response.url,
        terror_item['title'] = response.xpath('//*[@data-id ="f2eae65"]//text()').getall(),
        terror_item['reward'] = response.xpath('//*[@data-id ="5e60756"]//text()').getall(),
        terror_item['associated_organization'] = response.xpath('//*[@data-id ="b7c9ae6"]//text()').getall(),
        terror_item['associated_location'] = response.xpath('//*[@data-id ="0fa6be9"]//text()').getall(),
        terror_item['about'] = response.css('.elementor-widget-container p::text')[:-3].extract(),
        terror_item['image_url'] = response.css('.gallery-item a::attr(href)').get(),
        terror_item['dob'] = response.xpath('//*[@data-id ="9a896ea"]//text()').get(),
        yield terror_item