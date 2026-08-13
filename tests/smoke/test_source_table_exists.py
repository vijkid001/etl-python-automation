from config.db_connection import get_connection


def test_source_table_exists():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM all_tables
        WHERE owner = 'VIJAYSRC'
        AND table_name = 'PRODUCTS_SRC'
    """)

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    assert result == 1, "PRODUCTS_SRC table does not exist"