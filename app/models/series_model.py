import psycopg2
import os
from dotenv import load_dotenv

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

    def __init__(self, data) -> None:
        self.id, self.serie, self.seasons, self.released_date, self.genre, self.imdb_rating = data

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
