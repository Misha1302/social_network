from cursor import cursor


class SqliteDbCreator:
    def create_db_if_not_exists(self, cur: cursor):
        cur.execute("CREATE TABLE IF NOT EXISTS users(user_name, birth_date)")
        cur.execute("CREATE TABLE IF NOT EXISTS posts(owner_user_id, post_id, post_date, post_text)")
        cur.execute("CREATE TABLE IF NOT EXISTS message(msg_id, user1_id, user2_id, text)")
        cur.execute("CREATE TABLE IF NOT EXISTS images(image_id, using_in_post_id)")
