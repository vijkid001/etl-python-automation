import os

from tests.conftest import get_suite_data

smoke_data = get_suite_data("smoke_tests")[0]


def test_db_connection(source_connection):
    source_db = os.getenv("SOURCE_CONNECTION", "source_connection")
    source_type = os.getenv(f"{source_db}_TYPE", "unknown")
    source_schema = smoke_data["source_schema"]
    source_table = smoke_data["source_table_name"]
    source_query = smoke_data["source_table_exists_query"]

    print(f"\nSource DB      : {source_db} ({source_type})")
    print(f"Source schema  : {source_schema}")
    print(f"Source table   : {source_table}")
    print(f"Source query   : {source_query}")

    cursor = source_connection.cursor()
    assert cursor is not None

    cursor.execute(source_query)
    table_count = cursor.fetchone()[0]
    cursor.close()

    print(f"Table matches  : {table_count}")
    assert table_count > 0, (
        f"Source table {source_schema}.{source_table} was not found"
    )