from database.sqlite_cursor_provider import SqliteCursorProvider


class UserService:
    def add_user(self, name, birth_date):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(f"INSERT INTO users VALUES ('{name}', '{birth_date}')")

    def get_all_users(self):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()

    def get_users_with_this_name(self, name):
        with SqliteCursorProvider(None) as cursor:
            cursor.execute(f"SELECT * FROM users WHERE user_name = '{name}'")
            return cursor.fetchall()
