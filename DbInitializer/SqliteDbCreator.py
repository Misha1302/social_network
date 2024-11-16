class SqliteDbCreator:
    def create_db_if_not_exists(self, cursor):
        cursor.execute("CREATE TABLE IF NOT EXISTS users(user_name, birth_date)")
        cursor.execute("CREATE TABLE IF NOT EXISTS posts(owner_user_id, post_id, post_date, post_text)")
        cursor.execute("CREATE TABLE IF NOT EXISTS message(msg_id, user1_id, user2_id, text)")
        cursor.execute("CREATE TABLE IF NOT EXISTS images(image_id, using_in_post_id)")
