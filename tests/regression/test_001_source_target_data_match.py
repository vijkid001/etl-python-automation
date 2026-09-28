import pytest  # Testing framework used to manage test execution and assertions
from tests.conftest import get_suite_data


regression_data = get_suite_data("regression_tests")


@pytest.mark.priority1
@pytest.mark.data_match  # Custom marker to run data validation tests specifically
@pytest.mark.parametrize(
    "case", regression_data, ids=[case["name"] for case in regression_data]
)
def test_source_target_data_match(request, case):
    """Fetches data from source (Oracle) and target (Postgres) tables and verifies full data match."""

    source_connection = request.getfixturevalue(case["source"])
    target_connection = request.getfixturevalue(case["target"])

    source_table = f"{case['source_schema']}.{case['source_table_name']}"
    target_table = f"{case['target_schema']}.{case['target_table_name']}"

    # 3. Fetch all rows from Oracle (Source) sorted by primary key/ID for consistent comparison
    source_cursor = source_connection.cursor()  # Creates a cursor object to execute SQL commands on Oracle
    source_query = f"SELECT * FROM {source_table} ORDER BY 1"  # Query sorting by first column
    source_cursor.execute(source_query)  # Executes query on source Oracle DB
    source_data = source_cursor.fetchall()  # Retrives all rows as a list of tuples
    source_cursor.close()  # Closes source cursor session

    # 4. Fetch all rows from PostgreSQL (Target) sorted identically
    target_cursor = target_connection.cursor()  # Creates a cursor object to execute SQL commands on Postgres
    target_query = f"SELECT * FROM {target_table} ORDER BY 1"  # Query sorting by first column
    target_cursor.execute(target_query)  # Executes query on target Postgres DB
    target_data = target_cursor.fetchall()  # Retrieves all rows as a list of tuples
    target_cursor.close()  # Closes target cursor session

    # 5. Assertions - Verify row counts match before comparing cell values
    assert len(source_data) == len(target_data), (
        f"Row count mismatch! Source ({source_table}) has {len(source_data)} rows, "
        f"but Target ({target_table}) has {len(target_data)} rows."
    )

    # 6. Assertions - Verify actual data contents match row-by-row
    assert source_data == target_data, f"Data mismatch detected between {source_table} and {target_table}!"