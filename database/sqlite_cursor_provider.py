import sqlite3

from cursor import cursor


class SqliteCursorProvider:
    def __init__(self, config: dict | None, db_name="social_network.sqlite") -> None:
        self.configuration = config
        self.db_name = db_name

    def __enter__(self) -> cursor:
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cur.close()
        self.conn.close()
