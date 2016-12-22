#############################################################################################
# @Author : omkar nath                                                                      #
# @Email  : omkar  @startupflux.com                                                         #
# @About  : A script which scrapes site XML from alexa.com                                  #
#                                                                                           #
#         : '../settings.py' file to configure various spider settings.                     #
#         : '../items.py' contains definitions for the alexacompany StackItem               #
#         : '../pipelines.py' contains definitions for the mondoDB pipeline                 #
#############################################################################################
import scrapy
from pymongo import MongoClient

connection = MongoClient("ashmeet_mongodb_connection_string")
db = connection.students.ctec121
results = db.find()
print()
connection.close()
# temporary/fake mongodb db
'''
website_record = {}
flag = True

while (flag):
   website_name,website_link = input("Enter student name and link: ").split(',')
   website_record = {'name':website_name,'link':website_link}
   db.insert(website_record)
   flag = input('Enter another record? ')
   if (flag[0].upper() == 'N'):
      flag = False

    for record in results:
        print(record['name'] + ',',record['link'])
'''

class QuotesSpider(scrapy.Spider):
    name = "alexa"
    allowed_domains = ["alexa.com"]
    # start_url as mongodb db
    start_urls = results

    # start_url from txt file
    '''
    start_urls = [l.strip() for l in open('urls.txt').readlines()]
    
    >>> open('urls.txt').readlines()
    ['http://site.org\n', 'http://example.org\n', 'http://example.com/page\n']
    >>> [l.strip() for l in open('urls.txt').readlines()]
    ['http://site.org', 'http://example.org', 'http://example.com/page']
    
    f = open("urls.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()
    '''

    def parse(self, response):
        for url in urls:
            main_url = "http://data.alexa.com/data?cli=10&dat=snbamz&url=" + url
            version = response.css('#collapsible3')
            yield {
                'alexa_rank': response.css('#collapsible3 > div.expanded > div.collapsible-content > div:nth-child(2) > span > span > span.html-attribute-value::text').extract_first(),
                if not alexa_rank:
                    alexa_rank = None
                else:
                    alexa_rank = alexa_rank.strip()

                'country_code': response.css('#collapsible3 > div.expanded > div.collapsible-content > div:nth-child(4) > span > span:nth-child(1) > span.html-attribute-value').extract_first(),
                if not country_code:
                    country_code = None
                else:
                    country_code = country_code.strip()

                'country_name': response.css('#collapsible3 > div.expanded > div.collapsible-content > div:nth-child(4) > span > span:nth-child(2) > span.html-attribute-value').extract_first(),
                if not country_name:
                    country_name = None
                else:
                    country_name = country_name.strip()
                    
                'country_rank': response.css('#collapsible3 > div.expanded > div.collapsible-content > div:nth-child(4) > span > span:nth-child(3) > span.html-attribute-value').extract_first(),
                if not country_rank:
                    country_rank = None
                else:
                    country_rank = country_rank.strip()
            }

        