from database.sqlite_cursor_provider import SqliteCursorProvider
from database_Initializer.sqlite_db_creator import SqliteDbCreator


def init_db():
    with SqliteCursorProvider(None, "../social_network.sqlite") as cursor:
        SqliteDbCreator().create_db_if_not_exists(cursor)


init_db()
