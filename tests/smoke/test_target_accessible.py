from config.db_connection import get_connection


def test_target_accessible():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM VIJAYTGT.PRODUCTS_TGT
    """)

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    assert result >= 0