from cursor import cursor


class SqliteDbCreator:
    @staticmethod
    def create_db_if_not_exists(cur: cursor):
        cur.execute("CREATE TABLE IF NOT EXISTS users(user_id, user_name, user_password, user_email, birth_date)")
        cur.execute("CREATE TABLE IF NOT EXISTS posts(post_id, post_text, topic)")
        cur.execute("CREATE TABLE IF NOT EXISTS messages(msg_id, user1_id, user2_id, msg_text)")
        cur.execute("CREATE TABLE IF NOT EXISTS images(image_id, using_in_id)")
