import scrapy

# Define our Spider class
# First we set the name & then the domains the spider is allowed to scrape.
# Finally we tell the spider where to start scraping from.

class OscarsSpider(scrapy.Spider):
    name = "oscars"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ['https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture']

    # Next create a function which will capture the info we want.
    # We'll start with the page title & use CSS to find the tag with the title text.
    # Finally, we return the info back to Scrapy to be logged or written to a file.

    def parse(self, response):
        data = {}
        data['title'] = response.css('title::text').extract()
        yield data
