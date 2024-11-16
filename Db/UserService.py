from Db.SqliteCursorProvider import SqliteCursorProvider


class UserService:
    def add_user(self, name, birth_date):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(f"INSERT INTO users VALUES ('{name}', '{birth_date}')")

    def get_all_users(self):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
