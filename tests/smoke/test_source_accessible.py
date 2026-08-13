from config.db_connection import get_connection


def test_source_db_accessible():

    conn = get_connection()

    assert conn is not None

    conn.close()