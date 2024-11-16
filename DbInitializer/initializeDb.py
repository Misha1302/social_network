from Db.SqliteCursorProvider import SqliteCursorProvider
from DbInitializer.SqliteDbCreator import SqliteDbCreator


def init_db():
    with SqliteCursorProvider(None) as cursor:
        SqliteDbCreator().create_db_if_not_exists(cursor)
