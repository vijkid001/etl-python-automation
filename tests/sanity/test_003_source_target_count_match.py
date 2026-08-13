from config.db_connection import get_connection


def test_source_target_count_match():

    conn = get_connection()
    cursor = conn.cursor()

    # Get source count
    cursor.execute("""
        SELECT COUNT(*)
        FROM VIJAYSRC.PRODUCTS_SRC
    """)

    source_count = cursor.fetchone()[0]

    # Get target count
    cursor.execute("""
        SELECT COUNT(*)
        FROM VIJAYTGT.PRODUCTS_TGT
    """)

    target_count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    print(f"\nSource count : {source_count}")
    print(f"Target count : {target_count}")

    assert source_count == target_count, (
        f"Source and Target counts do not match. "
        f"Source={source_count}, Target={target_count}"
    )