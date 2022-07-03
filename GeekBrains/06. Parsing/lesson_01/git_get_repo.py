import requests
from pprint import pprint
import json

ENCODING = "utf-8"


class Git:
    API_URL = 'https://api.github.com/'

    @classmethod
    def check_connection_status(cls, response: requests):
        if response.status_code < 400:
            return True
        else:
            print(response.status_code)
            raise requests.HTTPError

    def __init__(self, account_name: str):
        self.account_name = account_name

    @property
    def _repo_data_vault(self) -> list:
        """ Получить лист метаданных по репозиториям """

        response = requests.get(self.API_URL + 'users/' + self.account_name + '/repos')
        if Git.check_connection_status(response):
            return response.json()

    @property
    def repo_list(self) -> list:
        """ Список репозиториев в человеческом виде """
        return [name['name'] for name in self._repo_data_vault]

    def get_repo(self, repo_name: str) -> dict:
        """ Получение доступа к мете определенного реопзитория (в виде словаря) """
        repo_index = self.repo_list.index(repo_name)
        return self._repo_data_vault[repo_index]


if __name__ == '__main__':
    file = 'git_get_repo.json'
    user = 'V-U-Simon'
    git_user = Git(user)

    # сохряняем список реопзиториев в json
    with open(file, 'a+', encoding=ENCODING) as f:

        to_save = json.dumps([user, git_user.repo_list])
        f.write(to_save + '\n')

    # читаем список реопзиториев в json
    with open(file, 'r', encoding=ENCODING) as f:
        for line in f:
            load_data = json.loads(line)
            pprint(load_data)