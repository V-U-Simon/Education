import requests
from pprint import pprint
import json




def ls_ya_drive(path):
    """ Чтение списка файлов в обласном хранилище """
    request_headers = {'Authorization': f'OAuth {TOKEN}'}
    url = f'https://cloud-api.yandex.net/v1/disk/resources?{path}'

    session = requests.session()
    response = session.get(url, headers=request_headers)
    folders = response.json()['_embedded']['items']

    return [folder['name'] for folder in folders]

if __name__ == '__main__':
    # todo: посмотреть корректные варианты хранения парлей и токенов (переменные окружения)
    TOKEN = '################'
    slash = '%2F'
    path = f'path={slash}'
    data = ls_ya_drive(path)
    file_json = 'ls_ya_disk.json'

    # write
    with open(file_json, 'w', encoding='UTF-8') as f:
        json.dump(data, f)

    # read
    with open(file_json, 'r', encoding='UTF-8') as f:
        data = json.load(f)
        pprint(data)
        # ['.debris', '1. Недвижимость', '2. Покупки', '3. ФЛ', '4. Банки', '4. ЮЛ', '5. Налоги',
        # '6. Суд', 'Code', 'Windows.11.RU-EN.16in1+-Office.2019.by.SmokieBlahBlah.2021.11.24',
        # 'X. АРХИВ', 'Загрузки', 'Книги']

