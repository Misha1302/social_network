from cursor import cursor


class SqliteDbCreator:
    def create_db_if_not_exists(self, cur: cursor):
        cur.execute("CREATE TABLE IF NOT EXISTS users(user_id, user_name, user_password, user_email, birth_date)")
        cur.execute("CREATE TABLE IF NOT EXISTS posts(owner_user_id, post_id, post_date, post_text)")
        cur.execute("CREATE TABLE IF NOT EXISTS messages(msg_id, user1_id, user2_id, msg_text)")
        cur.execute("CREATE TABLE IF NOT EXISTS images(image_id, using_in_id)")
