import scrapy


class QuotesSpider(scrapy.Spider):
    name = "movies"
    allowed_domains = ["yts.ag"] 
    start_urls = [
        'https://yts.ag/browse-movies',
        'https://yts.ag//browse-movies?page=%s' % page for page in range(296)
    ]

    def parse(self, response):
        for num in range(20):
            quote = response.css('body > div.main-content > div.browse-content > div > section > div > div:nth-child(%s)' % (num+1))
            yield{
                    'movie_details_page': quote.css('a.browse-movie-link::attr(href)').extract_first(),
                    'movie_name': quote.css('div.browse-movie-bottom a.browse-movie-title::text').extract_first(),
                    'relese_year': quote.css('div.browse-movie-bottom div.browse-movie-year::text').extract_first(),
                    '720p_torrent_link': quote.css('div.browse-movie-bottom div.browse-movie-tags a:nth-child(1)::attr(href)').extract_first(),
                    '1080p_torrent_link': quote.css('div.browse-movie-bottom div.browse-movie-tags a:nth-child(2)::attr(href)').extract_first(),
            }
        '''    
        next_page = response.css('body > div.main-content > div.browse-content > div > div:nth-child(6) > ul > li:nth-child(2) > a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        '''
            