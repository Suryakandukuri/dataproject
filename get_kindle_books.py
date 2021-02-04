import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Request, FormRequest
import pandas as pd


class KindleBooks(scrapy.Spider):\

    name = "kindlebooks"

    # initiating a booklist to append the data
    book_list = []

    def start_requests(self):
        # urls for the landing page and the second page on the amazon.com new releases in last 90 days
        start_urls = [
            "https://www.amazon.com/Deals-Kindle-Books-Last-90-days/s?rh=n%3A11552285011%2Cp_n_date%3A1249101011",
            "https://www.amazon.com/Deals-Kindle-Books-Last-90-days/s?i=digital-text&rh=n%3A11552285011%2Cp_n_date%3A1249101011&page=2&qid=1612474374&ref=sr_pg_2"
        ]
        for url in start_urls[:]:
            yield Request(
                url,
                callback= self.parse
            )


    def parse(self, response):

        # xpath value to get the names of the books and ratings
        book_names = response.xpath('//*[@class="a-size-medium a-color-base a-text-normal"]/text()').extract()

        rating_data = response.xpath('//*[@class="a-popover-trigger a-declarative"]/i/span/text()').extract()

        # making them a dataframe
        page_data = pd.DataFrame(
            {
                "book_name": book_names,
                "rating":rating_data
            }
        )
        # just to verify the data
        print(page_data)
        # appending it to the list
        self.book_list.append(page_data)
        
        pass
    # this works after the spider scrapes both the urls.
    def close(self, reason):
        # concating both the pages.
        kindle_books = pd.concat(self.book_list)
        kindle_books = kindle_books.reset_index(drop=True, inplace= False)
        # adding data to csv file.
        kindle_books.to_csv("kindle_ebooks_last90days.csv", index=False)



def main():
    """
    This is the script to scrape data from Amazon site, to get the
    Kindle Books that are released in the last 90 days
    
    Run the scraper as below.

    USAGE: python get_kindle_books.py
    """
    process = CrawlerProcess(
        settings={
            "USER_AGENT":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "ROBOTSTXT_OBEY": True
        }
    )
    process.crawl(KindleBooks)
    process.start()  # the script will block here until the crawling is finished


if __name__ == "__main__":
    main()