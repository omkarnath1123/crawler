import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["privco.com"]
    start_urls = [
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=&industry%5B%5D=100&industry%5B%5D=200&industry%5B%5D=300&industry%5B%5D=400&industry%5B%5D=500&industry%5B%5D=600&industry%5B%5D=700&industry%5B%5D=800&industry%5B%5D=900&industry%5B%5D=1000&industry%5B%5D=1100&industry%5B%5D=1200&industry%5B%5D=1300&industry%5B%5D=1400&industry%5B%5D=1500&industry%5B%5D=1600',
        ]

    
    '''

    quote = response.css('#search_results_content > div.table-responsive > table > tbody > tr:nth-child(1)')

    text = quote.css('td.col-name span.profile-name a::text').extract()
    data = quote.css('td.col-country a::text').extract()
    text_link = quote.css('td.col-name span.profile-name a::attr(href)').extract_first()
    type = quote.css('td.col-investor-type a::text').extract_first()
    state = quote.css('td.col-state a::text').extract_first()

    '''
    '''
    for num in range(25):
        quote = response.css('#search_results_content > div.table-responsive > table > tbody > tr:nth-child(num + 1)')

        Investor_name = quote.css('td.col-name span.profile-name a::text').extract_first()
        Investor_name_link = quote.css('td.col-name span.profile-name a::attr(href)').extract_first()
        country = quote.css('td.col-country a::text').extract_first()
        state_province = quote.css('td.col-state a::text').extract_first()
        Investor_type = quote.css('td.col-investor-type a::text').extract_first()



    value = response.css('#search_results_content > div.search-results-pagination')
    next_page = value.css('div.vertical-align div.text-right-lg ul.pagination li a::attr(href)').extract_first()
    if next_page is not None:
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)

    '''

    def parse(self, response):
        for num in range(25):
            quote = response.css('#search_results_content > div.table-responsive > table > tbody > tr:nth-child(%s)' % (num+1))
            yield{
                    'Investor_name' : quote.css('td.col-name span.profile-name a::text').extract_first(),
                    'Investor_name_link' : quote.css('td.col-name span.profile-name a::attr(href)').extract_first(),
                    'country' : quote.css('td.col-country a::text').extract_first(),
                    'state_province' : quote.css('td.col-state a::text').extract_first(),
                    'Investor_type' : quote.css('td.col-investor-type a::text').extract_first()
            }

        value = response.css('#search_results_content > div.search-results-pagination')
        next_page = value.css('div.vertical-align div.text-right-lg ul.pagination li a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


'''
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

'''