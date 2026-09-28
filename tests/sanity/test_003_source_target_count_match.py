import os


def test_source_target_count_match(
    source_connection,
    target_connection
):

    # ---------------------------------------------------------
    # Get selected database connections
    # ---------------------------------------------------------

    source_db = os.getenv("SOURCE_CONNECTION")
    target_db = os.getenv("TARGET_CONNECTION")

    assert source_db, "SOURCE_CONNECTION is not set in .env"
    assert target_db, "TARGET_CONNECTION is not set in .env"

    # ---------------------------------------------------------
    # Get schemas based on selected connections
    # ---------------------------------------------------------

    source_schema = os.getenv(f"{source_db}_SCHEMA")
    target_schema = os.getenv(f"{target_db}_SCHEMA")

    assert source_schema, (
        f"{source_db}_SCHEMA is not set in .env"
    )

    assert target_schema, (
        f"{target_db}_SCHEMA is not set in .env"
    )

    # ---------------------------------------------------------
    # SOURCE COUNT
    # ---------------------------------------------------------

    source_cursor = source_connection.cursor()

    source_cursor.execute(f"""
        SELECT COUNT(*)
        FROM {source_schema}.PRODUCTS_SRC
    """)

    source_count = source_cursor.fetchone()[0]

    source_cursor.close()

    # ---------------------------------------------------------
    # TARGET COUNT
    # ---------------------------------------------------------

    target_cursor = target_connection.cursor()

    target_cursor.execute(f"""
        SELECT COUNT(*)
        FROM {target_schema}.PRODUCTS_TGT
    """)

    target_count = target_cursor.fetchone()[0]

    target_cursor.close()

    # ---------------------------------------------------------
    # Display results
    # ---------------------------------------------------------

    print(f"\nSource DB     : {source_db}")
    print(f"Source Schema : {source_schema}")
    print(f"Source Count  : {source_count}")

    print(f"Target DB     : {target_db}")
    print(f"Target Schema : {target_schema}")
    print(f"Target Count  : {target_count}")

    # ---------------------------------------------------------
    # Compare
    # ---------------------------------------------------------

    assert source_count == target_count, (
        f"Source and Target counts do not match. "
        f"Source={source_count}, Target={target_count}"
    )


# import os
# import pytest


# def test_source_target_count_match(db_connection):
#     # Retrieve schema names directly from environment variables loaded via .env
#     source_schema = os.getenv("SOURCE_SCHEMA")
#     target_schema = os.getenv("TARGET_SCHEMA")

#     # Guard assertions: Fail early if schemas are missing or empty in .env
#     assert source_schema, "SOURCE_SCHEMA is not set or is empty in the .env file."
#     assert target_schema, "TARGET_SCHEMA is not set or is empty in the .env file."

#     # Use the connection fixture provided by conftest.py
#     cursor = db_connection.cursor()

#     # Query source count dynamically
#     cursor.execute(f"""
#         SELECT COUNT(*)
#         FROM {source_schema}.PRODUCTS_SRC
#     """)
#     source_count = cursor.fetchone()[0]

#     # Query target count dynamically
#     cursor.execute(f"""
#         SELECT COUNT(*)
#         FROM {target_schema}.PRODUCTS_TGT
#     """)
#     target_count = cursor.fetchone()[0]

#     cursor.close()

#     print(f"\nSource count : {source_count}")
#     print(f"Target count : {target_count}")

#     # Assert that record counts match
#     assert source_count == target_count, (
#         f"Source and Target counts do not match. "
#         f"Source={source_count}, Target={target_count}"
#     )