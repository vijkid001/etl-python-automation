import os

from tests.conftest import get_suite_data

smoke_data = get_suite_data("smoke_tests")[0]

def test_db_connection(target_connection, etl_config):
#def test_target_table_exists():
    #conn = get_connection()
    #cursor = conn.cursor()
    cursor = target_connection.cursor()
    target_table_data = etl_config["smoke_tests"][0]
    target_table_name = target_table_data["target_table_name"]
    target_table_query = target_table_data["target_table_exists_query"]

    #print(f"Target table_data   : {target_table_data}")
    print(f"Target table name   : {target_table_name}")
    print(f"Target table query   : {target_table_query}")

    cursor.execute(target_table_query)

    result = cursor.fetchone()[0]

    cursor.close()

    assert result == 1, f"{target_table_name} table does not exist"



# def test_db_connection(target_connection, etl_config):
# #def test_target_table_exists():
#     #conn = get_connection()
#     #cursor = conn.cursor()
#     cursor = target_connection.cursor()
#     target_table_data = etl_config["smoke_tests"][0]
#     target_table_name = target_table_data["target_table_name"]
#     target_table_query = target_table_data["target_table_exists_query"]

#     cursor.execute(target_table_query)

#     result = cursor.fetchone()[0]

#     cursor.close()

#     assert result == 1, f"{target_table_name} table does not exist"

#from config.db_connection import get_connection


# def test_db_connection(source_connection):
# #def test_target_table_exists():

#     cursor = source_connection.cursor()
#     # conn = get_connection()
#     # cursor = conn.cursor()

#     cursor.execute("""
#         SELECT COUNT(*)
#         FROM all_tables
#         WHERE owner = 'VIJAYTGT'
#         AND table_name = 'PRODUCTS_TGT'
#     """)

#     result = cursor.fetchone()[0]

#     cursor.close()
#     # conn.close()

#     assert result == 1, "PRODUCTS_TGT table does not exist"