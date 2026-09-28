import pytest


@pytest.mark.priority1
def test_source_record_count(source_connection, etl_config):
    source_data = etl_config["regression_tests"][0]
    source_query = source_data["source_record_count_query"].format(
        source_schema=source_data["source_schema"],
        source_table_name=source_data["source_table_name"],
    )

    print(f"\nSource schema   : {source_data['source_schema']}")
    print(f"Source table    : {source_data['source_table_name']}")
    print(f"Source query    : {source_query}")

    cursor = source_connection.cursor()
    cursor.execute(source_query)
    source_count = cursor.fetchone()[0]
    cursor.close()

    print(f"\nSource count    : {source_count}")





