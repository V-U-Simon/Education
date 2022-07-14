from __future__ import annotations
from lxml import html
import traceback
import requests
from pymongo import MongoClient
from fake_useragent import UserAgent
from collections import namedtuple

# MONGO_DB
client = MongoClient('localhost', 217)
db = client['news']
ya_news = db['yandex']

# DATA_FORMAT
News = namedtuple('News', 'title, link, source, date')

# SELECTORS yandex.ru
selector_content_list = "//section[@aria-labelledby='top-heading']/div/div"
selector_title = ".//h2/a/text()"
selector_source = ".//*[contains(@class,'source-link')]/text()"
selector_link = ".//*[contains(@class,'source-link')]/@href"
selector_date = ".//*[contains(@class,'source__time')]/text()"

# REQUEST
http_headers = {'User-Agent': UserAgent().chrome}
url: str = 'https://yandex.ru/news'
http_session = requests.session()
response = http_session.get(url, headers=http_headers)
dom = html.fromstring(response.text)
dom.text_content()


# PARSE
def parse_data(data) -> News:
    for el in data:
        try:
            title = el.xpath(selector_title)[0].replace('\xa0', ' ')
            link = el.xpath(selector_link)[0]
            source = el.xpath(selector_source)[0]
            date = el.xpath(selector_date)[0]

            return News(title, link, source, date)

        except Exception as e:
            print(f'parse error on {url}: {e}')
            print("traceback.print_exc():")
            traceback.print_exc()
            print("____")


if __name__ == '__main__':
    items = dom.xpath(selector_content_list)

    for item in items:
        news = parse_data(item)
        ya_news.insert_one(news._asdict())

    # Result into mongo_db
    # {
    # "_id" : ObjectId("62d3e6f9436029663ac4f786"),
    # "title" : "Минобороны: российские военные уничтожили в Одессе склад натовских ракет Harpoon",
    # "link" : "https://yandex.ru/news/story/Minoborony_rossijskie_voennye_unichtozhili_vOdesse_sklad_natovskikh_raket_Harpoon--0cc74db6b6b104a1dc2b8fede7de0cea?lang=ru&rubric=index&fan=1&stid=cW9C9vnOAcDK6xj7d4zD&t=1658053934&tt=true&persistent_id=217376261&story=9e465548-e63b-59b4-9137-762f86ed1d3b",
    # "source" : "РИА Новости", "date" : "13:32"
    # }
    # { "_id" : ObjectId("62d3e6f9436029663ac4f787"), "title" : "Разбившийся в Греции Ан-12 вез 11,5 т сербских вооружений в Бангладеш", "link" : "https://yandex.ru/news/story/Razbivshijsya_vGrecii_An-12_vez_115_t_serbskikh_vooruzhenij_vBangladesh--6b49a01efea662e6da6ae81d828121f9?lang=ru&rubric=index&fan=1&stid=5iKDBuAwoVGt3nFXO-Aa&t=1658053934&tt=true&persistent_id=217372391&story=924b7b5e-6a3b-58bb-b148-0466fd217a38", "source" : "РБК", "date" : "13:25" }
    # { "_id" : ObjectId("62d3e6f9436029663ac4f788"), "title" : "Депутат Госдумы Шеремет пригрозил сокрушительным ответом в случае удара по Крымскому мосту", "link" : "https://yandex.ru/news/story/Deputat_Gosdumy_SHeremet_prigrozil_sokrushitelnym_otvetom_vsluchae_udara_poKrymskomu_mostu--edbd08fed31d27aa86692909cb6b0232?lang=ru&rubric=index&fan=1&stid=adrf6O99niE_kch1NDYj&t=1658053934&tt=true&persistent_id=217375319&story=fd5a5734-140e-5794-9cd3-88df9f37da32", "source" : "Известия", "date" : "13:25" }
    # { "_id" : ObjectId("62d3e6f9436029663ac4f789"), "title" : "В Великобритании заявили о подготовке к войне с Россией", "link" : "https://yandex.ru/news/story/VVelikobritanii_zayavili_opodgotovke_kvojne_sRossiej--78e6ce1c7bedfd3c2bd3dd68ced41e52?lang=ru&rubric=index&fan=1&stid=AqwHjrMUrXGcKVyZdBdL&t=1658053934&tt=true&persistent_id=217301254&story=7c422419-ceae-5b5d-9acf-9dce68a944fd", "source" : "REGNUM", "date" : "13:25" }
    # { "_id" : ObjectId("62d3e6f9436029663ac4f78a"), "title" : "В минэкономики Германии заявили о невозможности пережить зиму без российского газа", "link" : "https://yandex.ru/news/story/Vminehkonomiki_Germanii_zayavili_onevozmozhnosti_perezhit_zimu_bezrossijskogo_gaza--ac9b4e4eae23a26d3f03bf9882c0b9c4?lang=ru&rubric=index&fan=1&stid=AgTsW4GkLZ6vlqKZKJQC&t=1658053934&tt=true&persistent_id=217371176&story=f1b0db5b-1eb7-584c-ab9a-9a3c7d90a4b0", "source" : "Коммерсантъ", "date" : "13:21" }