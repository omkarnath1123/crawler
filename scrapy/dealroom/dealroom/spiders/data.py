import scrapy
from scrapy_splash import SplashRequest
from selenium import webdriver
from scrapy.selector import Selector
from scrapy_splash import SplashRequest
from datetime import datetime

class MySpider(scrapy.Spider):
    name = "dealroom"
    start_urls = [
    "https://app.dealroom.co/companies", 
    ]
    def __init__(self):
        self.driver = webdriver.Firefox()

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 6},
                headers = {
                    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
                }
            )

    def parse(self, response):
        self.driver.get(response.url)
        value = 1
        while True:
            quote = response.css('#app > div > div > div.content-wrapper > div > div > div > div.table > div.virtual-list.table-list> div:nth-child(%s)'% value + 1)
            #app > div > div > div.content-wrapper > div > div > div > div.table > div.virtual-list.table-list > div:nth-child(1)
                    company_name = quote.css('div.table-list-column.name div.name-column-wrapper div.info div.name a::text').extract_first,
                    if not Investor_name:
                        continue

                    company_defination = quote.css('div.table-list-column.name > div.name-column-wrapper > div.info > div.tagline').extract_first,
                    if not company_defination:
                        item['company_defination'] = None
                    else:
                        item['company_defination'] = company_defination

                    company_garbage_link = quote.css('div.table-list-column.name div.name-column-wrapper div.info div.name a::attr(href)').extract_first,
                    if not company_garbage_link:
                        item['company_garbage_link'] = None
                    else:
                        item['company_garbage_link'] = company_garbage_link

                    company_tag = quote.css('div.table-list-column.name > div.name-column-wrapper > div.info > div.labels ').extract_first,
                    if not company_tag:
                        item['company_tag'] = None
                    else:
                        item['company_tag'] = company_tag

                    count = 0
                    total_tags = ""
                    for tags in company_tag:
                        span = tags.css('span:nth-child(%s)::text'%count + 1)
                        total_tags = total_tags + " ," + span
                        count = count + 1

                    company_tag = total_tags

                    company_industry = quote.css('div.table-list-column.industries > ul.item-list-column > li').extract_first,
                    if not company_industry:
                        item['company_industry'] = None
                    else:
                        item['company_industry'] = company_industry

                    count = 0
                    total_industry = ""
                    for name in company_industry:
                        value = name.css('a:nth-child(%s)::text'%count + 1)
                        total_industry = total_industry + " ," + value
                        count = count + 1

                    company_industry = total_industry

                    business_model = quote.css('div.table-list-column.revenues > div > ul.item-list-column.client-focus-list > li > a::text').extract_first,
                    if not business_model:
                        item['business_model'] = None
                    else:
                        item['business_model'] = business_model

                    ###########################################
                    
                    growth_stage = quote.css('').extract_first,
                    if not growth_stage:
                        item['growth_stage'] = None
                    else:
                        item['growth_stage'] = growth_stage

                    employees = quote.css('').extract_first,
                    if not employees:
                        item['employees'] = None
                    else:
                        item['employees'] = employees

                    growth_rank = quote.css('').extract_first,
                    if not growth_rank:
                        item['growth_rank'] = None
                    else:
                        item['growth_rank'] = growth_rank

                    funding = quote.css('').extract_first,
                    if not funding:
                        item['funding'] = None
                    else:
                        item['funding'] = funding

                    location = quote.css('').extract_first,
                    if not location:
                        item['location'] = None
                    else:
                        item['location'] = location

                    last_round = quote.css('').extract_first,
                    if not last_round:
                        item['last_round'] = None
                    else:
                        item['last_round'] = last_round

                    traffic = quote.css('').extract_first,
                    if not traffic:
                        item['traffic'] = None
                    else:
                        item['traffic'] = traffic

                    valuation = quote.css('').extract_first,
                    if not valuation:
                        item['valuation'] = None
                    else:
                        item['valuation'] = valuation

                    revenues = quote.css('').extract_first,
                    if not revenues:
                        item['revenues'] = None
                    else:
                        item['revenues'] = revenues

                    status = quote.css('').extract_first,
                    if not status:
                        item['status'] = None
                    else:
                        item['status'] = status

                    company_link = quote.css('').extract_first,
                    if not company_link:
                        item['company_link'] = None
                    else:
                        item['company_link'] = company_link

                    # for loop apppend
                    'company_tags'
                    'twitter_link' : quote.css('').extract_first,
                    'linkedin_link' : quote.css('').extract_first,
                    'CB_link' : quote.css('').extract_first,
                    'launch_date' : quote.css('').extract_first,
                    'ownership' : quote.css('').extract_first,
                    #json format
                    'funding_rounds'
                    'Investor_name' : quote.css('').extract_first(),
                    if not Investor_name:
                        item['Investor_name'] = None
                    else:
                        item['Investor_name'] = Investor_name

                    value = value + 1

                    #if Investor_type = None and Investor_name = None and Investor_name_link = None and country = None and state_province = None:
                        
            
            next = self.driver.find_element_by_xpath('//td[@class="pagn-next"]/a')

            try:
                #next.click()
                WebDriver driver = new FirefoxDriver();
                JavascriptExecutor jse = (JavascriptExecutor)driver;
                jse.executeScript("window.scrollBy(0,250)", "");
                # get the data and write it to scrapy items
            except:
                pass

        self.driver.close()

    
'''
class MySpider(scrapy.Spider):
    name = "deal"
    start_urls = [
    "https://app.dealroom.co/companies", 
    #"http://example.com/foo"
    ]

    def start_requests(self):
        for url in self.start_urls:
            #yield SplashRequest(url, self.parse,
            #    endpoint='render.html',
            #   args={'wait': 0.5},
            #)

            yield SplashRequest(
                url,
                self.parse,
                'http://example.com',
                endpoint='render.html',
                args={'js_source': 'document.title="My Title";'},
                args={'wait': 0.5},
            )

    def parse(self, response):
        # response.body is a result of render.html call; it
        # contains HTML processed by a browser.
'''