import os
import pytest


def test_source_target_count_match(db_connection):
    # Retrieve schema names directly from environment variables loaded via .env
    target_schema = os.getenv("TARGET_SCHEMA")
    

    # Guard assertions: Fail early if schemas are missing or empty in .env
    assert target_schema, "TARGET_SCHEMA is not set or is empty in the .env file."
    

    # Use the connection fixture provided by conftest.py
    cursor = db_connection.cursor()

    # Query target count dynamically
    # Query target count dynamically
    cursor.execute(f"""
        SELECT COUNT(*)
        FROM {target_schema}.PRODUCTS_TGT
    """)
    target_count = cursor.fetchone()[0]

    
    cursor.close()

    print(f"\ntarget count : {target_count}")

    
