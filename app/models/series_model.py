import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import sql
from typing import Union

from app.exc.series_exceptions import SeriesExceptions

load_dotenv()

configs = {
    "dbname": os.environ.get("DB_NAME"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "host": os.environ.get("DB_HOST")
}


def create_table():
    conn = psycopg2.connect(**configs)

    cur = conn.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS ka_series (
            id BIGSERIAL PRIMARY KEY,
            serie VARCHAR(100) NOT NULL UNIQUE,
            seasons INT NOT NULL,
            released_date DATE NOT NULL,
            genre VARCHAR(50) NOT NULL,
            imdb_rating FLOAT NOT NULL
        );
    """

    cur.execute(query)

    conn.commit()

    cur.close()
    conn.close()


class Series():

    def __init__(self, data: Union[tuple, dict]) -> None:
        if type(data) is tuple:
            self.id, self.serie, self.seasons, self.released_date, self.genre, self.imdb_rating = data

        elif type(data) is dict:
            for key, value in data.items():
                setattr(self, key, value)

    @staticmethod
    def list_all_series():

        conn = psycopg2.connect(**configs)

        cur = conn.cursor()

        query = """ SELECT * FROM ka_series;"""

        cur.execute(query)

        results = cur.fetchall()

        conn.commit()

        cur.close()
        conn.close()

        list_results = [Series(serie).__dict__ for serie in results]

        return list_results

    @staticmethod
    def list_serie_by_id(id):

        conn = psycopg2.connect(**configs)

        cur = conn.cursor()

        cur.execute(f'SELECT * FROM ka_series WHERE id=(%s);', (id,))

        results = cur.fetchone()

        if not results:
            raise SeriesExceptions(f"serie com id {id} não encontrado.")

        conn.commit()

        cur.close()
        conn.close()

        result = Series(results).__dict__

        return result

    def create_serie(self):

        columns = [sql.Identifier(key) for key in self.__dict__.keys()]
        values = [sql.Literal(value) for value in self.__dict__.values()]

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        query = sql.SQL("""
            INSERT INTO
                ka_series (id, {columns})
            VALUES
                (DEFAULT, {values})
            RETURNING *
        """).format(columns=sql.SQL(',').join(columns), values=sql.SQL(',').join(values))

        cur.execute(query)

        fetch_result = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        serialized_data = Series(fetch_result).__dict__

        return serialized_data

    @staticmethod
    def delete(id):

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        cur.execute(f"DELETE FROM ka_series WHERE id=(%s) RETURNING *;", (id,))

        fetch_result = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        if not fetch_result:
            raise SeriesExceptions(f"serie com id {id} não encontrado.")

        serialized_data = Series(fetch_result).__dict__

        return serialized_data

    @staticmethod
    def update(id: int, data):

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        columns = [sql.Identifier(key) for key in data.keys()]
        values = [sql.Literal(value) for value in data.values()]

        query = sql.SQL(
            """
                UPDATE
                    ka_series
                SET
                    ({columns}) = row({values})
                WHERE
                    id={id}
                RETURNING *
            """).format(id=sql.Literal(str(id)),
                        columns=sql.SQL(',').join(columns),
                        values=sql.SQL(',').join(values))

        cur.execute(query)

        fetch_result = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        if not fetch_result:
            raise SeriesExceptions(f"serie com id {id} não encontrado.")

        serialized_data = Series(fetch_result).__dict__

        return serialized_data
