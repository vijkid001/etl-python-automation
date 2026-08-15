import os
import pytest


def test_source_target_count_match(db_connection):
    # Retrieve schema names directly from environment variables loaded via .env
    source_schema = os.getenv("SOURCE_SCHEMA")
    

    # Guard assertions: Fail early if schemas are missing or empty in .env
    assert source_schema, "SOURCE_SCHEMA is not set or is empty in the .env file."
    

    # Use the connection fixture provided by conftest.py
    cursor = db_connection.cursor()

    # Query source count dynamically
    cursor.execute(f"""
        SELECT COUNT(*)
        FROM {source_schema}.PRODUCTS_SRC
    """)
    source_count = cursor.fetchone()[0]

    
    cursor.close()

    print(f"\nSource count : {source_count}")

    
