import os

import pytest
from tests.conftest import get_suite_data

smoke_data = get_suite_data("smoke_tests")


@pytest.mark.priority1
@pytest.mark.parametrize(
    "case", smoke_data, ids=[case["name"] for case in smoke_data]
)
def test_smoke_db_connections(request, case):
    source_conn = request.getfixturevalue(case["source"])
    target_conn = request.getfixturevalue(case["target"])

    source_db = os.getenv("SOURCE_CONNECTION", case["source"])
    target_db = os.getenv("TARGET_CONNECTION", case["target"])
    source_schema = case.get("source_schema", "not specified")
    target_schema = case.get("target_schema", "not specified")
    print(f"\nSource DB      : {source_db} ({os.getenv(f'{source_db}_TYPE', 'unknown')})")
    print(f"Source schema  : {source_schema}")
    print(f"Source query   : {case['source_query']}")

    with source_conn.cursor() as cur:
        cur.execute(case["source_query"])
        assert cur.fetchone()[0] == "CONNECTED"

    print(f"Target DB      : {target_db} ({os.getenv(f'{target_db}_TYPE', 'unknown')})")
    print(f"Target schema  : {target_schema}")
    print(f"Target query   : {case['target_query']}")

    with target_conn.cursor() as cur:
        cur.execute(case["target_query"])
        assert cur.fetchone()[0] == "CONNECTED"



############### 2.0 #######################
# def test_db_connection(source_connection):

#     cursor = source_connection.cursor()

#     cursor.execute("SELECT 'CONNECTED' FROM dual")

#     result = cursor.fetchone()

#     cursor.close()

#     assert result[0] == "CONNECTED"

############### 2.0 #######################

############### 1.0 #######################

# from config.db_connection import get_connection

# def test_db_connection():

#     conn = get_connection()

#     cursor = conn.cursor()

#     cursor.execute("SELECT 'CONNECTED' FROM dual")

#     result = cursor.fetchone()

#     assert result[0] == "CONNECTED"

#     cursor.close()
#     conn.close()

############### 1.0 #######################