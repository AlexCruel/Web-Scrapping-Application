import scrapy
import xlsxwriter

class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):

        workbook = xlsxwriter.Workbook('author.xlsx')
        worksheet = workbook.add_worksheet()

        def extract_with_css(query, worksheet):
            worksheet.write('A1', 'Hello, World!')
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('.author-title::text', worksheet),
            'birthdate': extract_with_css('.author-born-date::text', worksheet),
            'bio': extract_with_css('.author-description::text', worksheet)
        }

        workbook.close()