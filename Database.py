import sqlite3

DB_NAME = "social_network.sqlite"


class Database:
    def __init__(self):
        self.inited = True
        self.connection = None
        self.cursor = None

        self.init()

    def __enter__(self):
        if not self.inited:
            self.init()
        return self

    def _execute(self, request):
        res = self.cursor.execute(request)
        self.connection.commit()
        return res.fetchall()

    def add_user(self, name, birth_date):
        self._execute(f"INSERT INTO users VALUES ('{name}', '{birth_date}')")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def init(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.cursor = self.connection.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(user_name, birth_date)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS posts(owner_user_id, post_id, post_date, post_text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS message(msg_id, user1_id, user2_id, text)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS images(image_id, using_in_post_id)")
