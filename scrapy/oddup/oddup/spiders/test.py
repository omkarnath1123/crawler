#############################################################################################
# @Author : Omkar Nath                                                                      #
# @Email  : omkar@startupflux.com                                                           #
# @About  : A script which scrapes site data from oddup.com                                 #
#                                                                                           #
#         : '../settings.py' file to configure various spider settings in splash.           #
#         : '../items.py' contains definitions for the oddupcompany StackItem               #
#         : '../pipelines.py' contains definitions for the mondoDB pipeline                 #
#############################################################################################

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = 'C:\\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)
browser.get('http://www.oddup.com')

username = selenium.find_element_by_id("username")
password = selenium.find_element_by_id("password")

username.send_keys("YourUsername")
password.send_keys("Pa55worD")

selenium.find_element_by_name("submit").click()
'''
import scrapy
from scrapy_splash import SplashRequest

class LoginSpider(scrapy.Spider):
    name = 'oddup'
    allowed_domains = ["oddup.com"]
    start_urls = [
        'http://www.oddup.com/analysis/investors',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )

    def parse(self, response):
        yield SplashRequest(
            'http://www.oddup.com/analysis/investors',
            endpoint='render.html',
            args={'js_source': 'document.title="Oddup";'},
        )
        '''
        yield scrapy.Request(url, self.parse_result, meta={
            'splash': {
                'args': {
                    # set rendering arguments here
                    'html': 1,
                    'png': 1,

                    # 'url' is prefilled from request url
                    # 'http_method' is set to 'POST' for POST requests
                    # 'body' is set to request body for POST requests
                },

                # optional parameters
                'endpoint': 'render.json',  # optional; default is render.json
                'splash_url': 'http://www.oddup.com/analysis/investors',      # optional; overrides SPLASH_URL
                'slot_policy': scrapy_splash.SlotPolicy.PER_DOMAIN,
                'splash_headers': {},       # optional; a dict with headers sent to Splash
                'dont_process_response': True, # optional, default is False
                'dont_send_headers': True,  # optional, default is False
                'magic_response': False,    # optional, default is True
            }
        })
        '''
        '''
        function main(splash)
            assert(splash:go(splash.args.url))
            splash:wait(0.5)
            local title = splash:evaljs("document.title")
            return {title=title}
        end

        {
            "title": "Some title"
        }
        '''
        '''
        function main(splash)
            assert(splash:go(splash.args.url))
            local get_dimensions = splash:jsfunc([[
                function () {
                    var rect = document.getElementById('button').getClientRects()[0];
                    return {"x": rect.left, "y": rect.top}
                }
            ]])
            splash:set_viewport_full()
            splash:wait(0.1)
            local dimensions = get_dimensions()
            splash:mouse_click(dimensions.x, dimensions.y)
            -- Wait split second to allow event to propagate.
            splash:wait(0.1)
            return splash:html()
        end
        '''
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'omkar@startupflux.com', 'password': '9818271889Abc'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
        for num in range(6):
            quote = response.css('#react-root > div > main > div.p-analysis > section > ul > li:nth-child(%s)' %(num + 2))
            yield {
                'company_name': quote.css('div.analysisList-field-fixed div.analysisList-companyName a::text').extract_first(),
                #'company_score': quote.css('span.text::text').extract_first(),
                'company_link': quote.css('div.analysisList-field-fixed div.analysisList-companyName a::attr(href)').extract_first(),
                #'social_score': quote.css('div.tags a.tag::text').extract_first(),
                #'Trascation_score': quote.css('div.tags a.tag::text').extract_first(),
                'TotalFunding': quote.css('div.analysisList-field.analysisList-totalFunding::text').extract_first(),
                'LatestFunding': quote.css('div.analysisList-field.analysisList-totalFunding.latest::text').extract_first(),
                'currentValue': quote.css('div.analysisList-field.analysisList-currentValuation::text').extract_first(),
                'futureValue': quote.css('div.analysisList-field.analysisList-futureValuation::text').extract_first(),
                'View': quote.css('div.analysisList-field.analysisList-view div.analysisList-ratingInProgress.textTransfromNone::text').extract_first(),
                'Expectation': quote.css('div.analysisList-field.analysisList-expectation::text').extract_first(),
                'Industry': quote.css('div.analysisList-field.analysisList-industry::text').extract_first(),
                'Location': quote.css('div.analysisList-field.analysisList-location a::text').extract_first(),
                'Location_link': quote.css('div.analysisList-field.analysisList-location a::attr(href)').extract_first(),
                'Followers_oddup': quote.css('div.analysisList-field.analysisList-follower::text').extract_first(),
            }
            value = response.css('#react-root > div > main > div.p-analysis > div.reactPaginate')
            next_page = value.css('ul.pagination a').extract_first()
            if next_page is not None:
                # splash:runjs("$('next-element-css').click()")
                #next_page = response.urljoin(next_page)
                #yield scrapy.Request(next_page, callback=self.parse)
                pass