import scrapy


class QuotesSpider(scrapy.Spider):
    name = "privko"
    allowed_domains = ["privco.com"]
    start_urls = [
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=&industry%5B%5D=100&industry%5B%5D=200&industry%5B%5D=300&industry%5B%5D=400&industry%5B%5D=500&industry%5B%5D=600&industry%5B%5D=700&industry%5B%5D=800&industry%5B%5D=900&industry%5B%5D=1000&industry%5B%5D=1100&industry%5B%5D=1200&industry%5B%5D=1300&industry%5B%5D=1400&industry%5B%5D=1500&industry%5B%5D=1600',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001001&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go/page/1?region%5B0%5D=0001001&investment_activity=-1&date_min=&date_max=&industry_classification_type=&industry_code=&include_industry_unknown=&location_input_text=&postal_range=500&postal_zip_code=&sort_name=ASC',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001002&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001003&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001004&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001005&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001006&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001007&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001008&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001009&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001010&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001011&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001012&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001013&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001014&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001015&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001016&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001017&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001018&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001019&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001020&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001021&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001022&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001023&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001024&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001025&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001026&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001027&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001028&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001029&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001030&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001031&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001032&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001033&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001034&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001035&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001036&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001037&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001038&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001039&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001040&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001041&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001042&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001043&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001044&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001045&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001046&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001047&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001048&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001049&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001050&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001051&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0001052&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002001&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002002&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002003&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002004&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002005&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002006&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002007&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002008&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002009&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002010&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002011&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002012&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0002013&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0010&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003001&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003012&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003019&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003017&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003013&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003014&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003003&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003002&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003006&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003015&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003021&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003004&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003011&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003009&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003008&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003018&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003010&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003020&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003022&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003016&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003005&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003007&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0003023&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0004&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005001&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005002&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005003&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005004&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005010&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005007&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005012&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005011&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005008&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005005&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005006&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0005009&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0006&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0006&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0007&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0007001&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0007002&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0007003&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0007004&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0009&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0008&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0008001&postal_zip_code=&location_input_text=&postal_range=25&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0008003&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
        'http://www.privco.com/investors/advanced-search/go?region%5B%5D=0008002&postal_zip_code=&location_input_text=&postal_range=500&investor_type%5B%5D=&investment_activity=-1&date_min=&date_max=&preferred_stages%5B%5D=&f_ind_q=',
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
'''
BOT_NAME = 'example'

SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

#LOG_LEVEL = 'INFO'

CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 5
USER_AGENT = 'WebScrapingWithPython'

'''