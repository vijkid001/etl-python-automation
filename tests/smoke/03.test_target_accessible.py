import os

from tests.conftest import get_suite_data

smoke_data = get_suite_data("smoke_tests")[0]


def test_db_connection(target_connection):
    target_db = os.getenv("TARGET_CONNECTION", "target_connection")
    target_type = os.getenv(f"{target_db}_TYPE", "unknown")
    target_schema = smoke_data["target_schema"]
    target_table = smoke_data["target_table_name"]
    target_query = smoke_data["target_table_exists_query"]

    print(f"\nTarget DB      : {target_db} ({target_type})")
    print(f"Target schema  : {target_schema}")
    print(f"Target table   : {target_table}")
    print(f"Target query   : {target_query}")

    cursor = target_connection.cursor()
    assert cursor is not None

    cursor.execute(target_query)
    table_count = cursor.fetchone()[0]
    cursor.close()

    print(f"Table matches  : {table_count}")
    assert table_count > 0, (
        f"Target table {target_schema}.{target_table} was not found"
    )


# def test_db_connection(target_connection, etl_config):
#     cursor = target_connection.cursor()

#     assert cursor is not None

#     cursor.close()
