from sqlalchemy import create_engine

class Postgres:
    url = ''

    def __init__(self, url):
        self.url = url

    def Engine(self):
        try:
            return create_engine(self.url, encoding='utf-8')
        except Exception as e:
            print(e)
