# import scrapy

# class TerrorSpider(scrapy.Spider):
#     name = 'terrorspider'
#     allowed_domains = ['rewardsforjustice.net']
#     start_urls = ['http://rewardsforjustice.net/rewards/']

#     def parse(self, response):
        
#         terrors = response.css('div.page-content')
#         for terror in terrors:
#             terror_url = terror.css('h2.entry-title a::attr(href)').get()
            
#             yield response.follow(terror_url, callback = self.parse_terror_page)
            
#             # yield scrapy.Request(url=terror_url, callback=self.parse_terror)
        
#         # Extracting URL for next page
#         next_page = response.css('div.nav-previous a::attr(href)').get()
#         if next_page is not None:
#             next_page_url = next_page
#             yield response.follow(next_page_url, callback=self.parse)

#     def parse_terror(self, response):
#         # Extracting data from terror page
        
#         associated_locations =  response.xpath('//*[@data-id ="0fa6be9"]//text()').getall()
#         associated_location =", ".join([word for word in associated_locations if word.strip(", ")])
#         # Known_Locals = response.xpath('//*[@data-id ="169d745"]//text()').getall()
#         # known_local = ", ".join([local for local in Known_Locals if local.strip(", ")])

#         associated_organization_text = response.xpath('//*[@data-id ="b7c9ae6"]//text()').getall()
#         # Extract only the strings, removing semicolons and any extra spaces
#         associated_organization = ", ".join([text.strip().replace(";", "") for text in associated_organization_text[0].split(";\xa0")])
#         # Join the cleaned strings into a single string
#         yield { 
#             'url': response.url,
#             # 'title' : response.css('.elementor-element.elementor-element-f2eae65.elementor-widget.elementor-widget-heading ::text').get(),
#             'title' : response.xpath('//*[@data-id ="f2eae65"]//text()').getall()[0],
#             'about': "\n".join(response.css('.elementor-widget-container p::text')[:-3].extract()),
#             'image_url' : response.css('.gallery-item a::attr(href)').get(),
#             'dob' : response.xpath('//*[@data-id ="9a896ea"]//text()').get(),
#             'associated_location' : associated_location,
#             # 'known_local' : known_local
#             'associated_organization' : associated_organization,
#             'Reward' : response.xpath('//*[@data-id ="5e60756"]//text()').getall()[0]
#             }
        


        # associated_locations =  response.xpath('//*[@data-id ="0fa6be9"]//text()').getall()
        # associated_location =", ".join([word for word in associated_locations if word.strip(", ")])
        # associated_organization_text = response.xpath('//*[@data-id ="b7c9ae6"]//text()').getall()
        # # Extract only the strings, removing semicolons and any extra spaces
        # associated_organization = ", ".join([text.strip().replace(";", "") for text in associated_organization_text[0].split(";\xa0")])
