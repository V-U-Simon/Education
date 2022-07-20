import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


# from jobparser.items import JobparserItem


class HhruSpider(scrapy.Spider):
    vacancy = 'python'
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = [
        f"https://hh.ru/search/vacancy?area=1&items_on_page=20&text={vacancy}&order_by=salary_asc",
        f"https://hh.ru/search/vacancy?area=3&items_on_page=20&text={vacancy}&order_by=salary_asc",
        f"https://hh.ru/search/vacancy?area=3&items_on_page=20&text={vacancy}&order_by=salary_desc",
        f"https://hh.ru/search/vacancy?area=3&items_on_page=20&text={vacancy}&order_by=salary_desc",
        f"https://hh.ru/search/vacancy?area=1&items_on_page=20&text={vacancy}&order_by=publication_time",
        f"https://hh.ru/search/vacancy?area=3&items_on_page=20&text={vacancy}&order_by=publication_time",
    ]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@data-qa='vacancy-serp__vacancy-title']/@href").getall()
        if links:
            for link in links:
                yield response.follow(link, callback=self.vacancy_parse)


    def vacancy_parse(self, response: HtmlResponse):
        print('*' * 70, 'vacancy_parse')
        _id = response.url
        name = response.xpath("//h1/text()").get()
        description = response.xpath("//div[@data-qa='vacancy-description']//text()").getall()
        skills = response.xpath("//div[@class='bloko-tag-list']//text()").getall()
        location = response.xpath("//p[@data-qa='vacancy-view-location']//text()").get()
        salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        tax_include = response.xpath("//div[@data-qa='vacancy-salary']//node()").attrib['data-qa']
        url = response.url
        company = response.xpath("//a[@data-qa='vacancy-company-name']//text()").getall()
        company_id = response.xpath("//a[@data-qa='vacancy-company-name']//@href").get()
        company_link = response.xpath("//a[@data-qa='vacancy-company-name']//@href").get()

        yield JobparserItem(_id=_id,
                            name=name,
                            description=description,
                            skills=skills,
                            location=location,
                            salary=salary,
                            tax_include=tax_include,
                            url=url,
                            company=company,
                            company_id=company_id,
                            company_link=company_link)
