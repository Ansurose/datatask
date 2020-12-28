import scrapy
from scrapy.http import Request
from eventtask.items import EventtaskItem 

class EventtaskSpider(scrapy.Spider):
	name = 'Events'
	allowed_domians = ['allevents.in']
	
	
	def start_requests(self):
		start_urls = "https://allevents.in/new delhi/all"
		headers={
			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
			'authority': 'allevents.in',
			'method': 'GET',
			'path': '/new%20delhi/all',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9,ml;q=0.8',
			'cache-control': 'max-age=0'
			}
		yield Request(start_urls, headers=headers, callback=self.parse)



	
	def parse(self, response):
		
		for event_url in response.xpath(".//ul[@class='resgrid-ul']//a/@href").extract():
			headers={
			'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
			'authority': 'allevents.in',
			'method': 'GET',
			'path': '/new%20delhi/all',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9,ml;q=0.8',
			'cache-control': 'max-age=0'
			}
			yield Request(response.urljoin(event_url), callback=self.parse_all__event,headers=headers)
		
	def parse_all__event(self, response):
			#iscription =[list(filter(None,[text.strip() for text in ev.css('div[class="event-description-html"]').css(' *::text').extract()])) for ev in response.xpath('//*[@id="event-detail-fade"]/div[3]/div[1]/div[1]')]
			#scription = [''.join(des) for des in description]
			yield EventtaskItem(
			event_name = response.xpath("//div[@class='padding-10 head-details hidden-phone']/h1/text()").getall(),
			address = response.xpath("////span[@class='full-venue']/text()").extract(),
			image= response.xpath("////img[@property='schema:image']/@src").extract(),
			org_name = response.xpath("////div[@class='name']/span/a/text()").extract(),
			org_url = response.xpath("//div[@class='name']//a/@href").extract(),
			org_image = response.xpath("////div[@class='thumb']/a/img/@src").extract(),
			#escription = description

			)
			next_page = response.xpath("//*[@id='event_list']/div[2]/div[2]/div/a/@href").extract()
			if next_page is not None:
			
				yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
	
