def test_target_record_count(target_connection, etl_config):
    target_data = etl_config["regression_tests"][0]
    target_query = target_data["target_record_count_query"].format(
        target_schema=target_data["target_schema"],
        target_table_name=target_data["target_table_name"],
    )

    print(f"\nTarget schema   : {target_data['target_schema']}")
    print(f"Target table    : {target_data['target_table_name']}")
    print(f"Target query    : {target_query}")

    cursor = target_connection.cursor()
    cursor.execute(target_query)
    target_count = cursor.fetchone()[0]
    cursor.close()

    print(f"\nTarget count    : {target_count}")







# import os
# import pytest


# def test_source_target_count_match(db_connection):
#     # Retrieve schema names directly from environment variables loaded via .env
#     target_schema = os.getenv("TARGET_SCHEMA")
    

#     # Guard assertions: Fail early if schemas are missing or empty in .env
#     assert target_schema, "TARGET_SCHEMA is not set or is empty in the .env file."
    

#     # Use the connection fixture provided by conftest.py
#     cursor = db_connection.cursor()

#     # Query target count dynamically
#     # Query target count dynamically
#     cursor.execute(f"""
#         SELECT COUNT(*)
#         FROM {target_schema}.PRODUCTS_TGT
#     """)
#     target_count = cursor.fetchone()[0]

    
#     cursor.close()

#     print(f"\ntarget count : {target_count}")

    
