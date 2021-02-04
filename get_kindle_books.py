import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Request, FormRequest


class KindleBooks(scrapy.Spider):\

    name = "kindlebooks"

    book_list = []

    def start_requests(self):
        start_urls = [
            "https://www.amazon.com/Deals-Kindle-Books-Last-90-days/s?rh=n%3A11552285011%2Cp_n_date%3A1249101011"
        ]
        for url in start_urls:
            yield Request(
                url,
                callback= self.parse
            )
            # yield FormRequest(
            #     url = url,
            #     method = "GET",
            #     formdata= {
            #         "bbn":"11552285011",
            #         "rh":"n:11552285011,p_n_date:1249101011",
            #         "dc":"",
            #         "qid":"1612457524",
            #         "rnid":"1249099011",
            #         "ref":"lp_11552285011_nr_p_n_date_1"
            #     },
            #     callback=self.parse,
            # )

    def parse(self, response):

        print(response.text)

        # book_data = response.css("sg-col-inner").extract()

        # last_90_link = response.xpath(
        #     '//*[@class="a-unordered-list a-nostyle a-vertical a-spacing-medium"]/li/span/a'
        # ).extract()

        # print(last_90_link)
        


def main():
    """
    This is the script to scrape data from Amazon site, to get the
    Kindle Books that are released in the last 90 days
    
    Run the scraper as below.

    USAGE: python get_kindle_books.py
    """
    process = CrawlerProcess(
        settings={
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            # Uncomment lines below to add download_delay and concurrent_requests to crawler settings
            # "DOWNLOAD_DELAY": 0.25,  # 250 milliseconds
            # "CONCURRENT_REQUESTS": 3,
            # Set the download timeout
            # "DOWNLOAD_TIMEOUT": 300,
            # Set robotstxt_obey to False
            # "ROBOTSTXT_OBEY": False,
            # Item pipeline for catalog
            # "ITEM_PIPELINES": {"factly.scrape.pipelines.SaveCatalogCSV": 10},
        }
    )
    process.crawl(KindleBooks)
    process.start()  # the script will block here until the crawling is finished


if __name__ == "__main__":
    main()