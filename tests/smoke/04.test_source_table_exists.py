#from config.db_connection import get_connection

import os

from tests.conftest import get_suite_data

smoke_data = get_suite_data("smoke_tests")[0]

def test_db_connection(source_connection, etl_config):
#def test_source_table_exists():
    #conn = get_connection()
    #cursor = conn.cursor()
    cursor = source_connection.cursor()
    source_table_data = etl_config["smoke_tests"][0]
    source_table_name = source_table_data["source_table_name"]
    source_table_query = source_table_data["source_table_exists_query"]

    #print(f"Source table_data   : {source_table_data}")
    print(f"Source table name   : {source_table_name}")
    print(f"Source table query   : {source_table_query}")


    cursor.execute(source_table_query)

    result = cursor.fetchone()[0]

    cursor.close()
    #conn.close()

    assert result == 1, f"{source_table_name} table does not exist"




# def test_db_connection(source_connection, etl_config):
# #def test_source_table_exists():
#     #conn = get_connection()
#     #cursor = conn.cursor()
#     cursor = source_connection.cursor()
#     source_table_data = etl_config["smoke_tests"][0]
#     source_table_name = source_table_data["source_table_name"]
#     source_table_query = source_table_data["source_table_exists_query"]

#     cursor.execute(source_table_query)

#     result = cursor.fetchone()[0]

#     cursor.close()
#     #conn.close()

#     assert result == 1, f"{source_table_name} table does not exist"


    