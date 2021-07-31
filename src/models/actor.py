from sqlalchemy.engine.base import Connection, Engine
from sqlalchemy.sql.expression import text
from src.models.postgres import Postgres
from src.utils.env import getenv


class Actor:
    engine: Engine or None = None

    def __init__(self) -> None:
        try:
            engine = Postgres(getenv('URL')).Engine()
            self.engine = engine
        except Exception as e:
            print(e)

    def all(self):
        query = "SELECT * FROM actor"
        engine_connected: Connection = self.engine.connect()
        try:
            records = engine_connected.execute(text(query))
            return records
        except Exception as e:
            print('Get all Actor Error:', e)
        finally:
            engine_connected.close()
