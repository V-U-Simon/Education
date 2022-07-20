from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings  # импортируем настройки
from scrapy.utils.log import configure_logging

# import my spiders
from jobparser.spiders.hhru import HhruSpider

if __name__ == '__main__':
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    settings = get_project_settings()  # настройки
    runner = CrawlerRunner(settings)

    d = runner.crawl(HhruSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()  # the script will block here until the crawling is finished
