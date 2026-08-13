from config.db_connection import get_connection


def test_target_table_exists():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM all_tables
        WHERE owner = 'VIJAYTGT'
        AND table_name = 'PRODUCTS_TGT'
    """)

    result = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    assert result == 1, "PRODUCTS_TGT table does not exist"