from config.db_connection import get_connection


def test_db_connection():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT 'CONNECTED' FROM dual")

    result = cursor.fetchone()

    assert result[0] == "CONNECTED"

    cursor.close()
    conn.close()