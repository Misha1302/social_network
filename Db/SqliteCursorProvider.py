import sqlite3

from cursor import cursor


class SqliteCursorProvider:
    DB_NAME = "social_network.sqlite"

    def __init__(self, config: dict | None) -> None:
        self.configuration = config

    def __enter__(self) -> "cursor":
        self.conn = sqlite3.connect(self.DB_NAME)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
