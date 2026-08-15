import os


def test_primary_key_not_null(db_connection):
    source_schema = os.getenv("SOURCE_SCHEMA")
    target_schema = os.getenv("TARGET_SCHEMA")

    assert source_schema, "SOURCE_SCHEMA is not set or is empty in the .env file."
    assert target_schema, "TARGET_SCHEMA is not set or is empty in the .env file."

    cursor = db_connection.cursor()

    for schema_name, table_name in [
        (source_schema, "PRODUCTS_SRC"),
        (target_schema, "PRODUCTS_TGT"),
    ]:
        cursor.execute(
            """
            SELECT c.column_name
            FROM all_constraints cons
            JOIN all_cons_columns c
                ON cons.owner = c.owner
               AND cons.constraint_name = c.constraint_name
            WHERE cons.owner = :schema_name
              AND cons.table_name = :table_name
              AND cons.constraint_type = 'P'
            ORDER BY c.position
            """,
            {"schema_name": schema_name.upper(), "table_name": table_name.upper()},
        )

        primary_key_columns = [row[0] for row in cursor.fetchall()]
        assert primary_key_columns, (
            f"{schema_name}.{table_name} does not have a primary key defined."
        )

        for column_name in primary_key_columns:
            cursor.execute(
                f"""
                SELECT COUNT(*)
                FROM {schema_name}.{table_name}
                WHERE {column_name} IS NULL
                """
            )
            null_count = cursor.fetchone()[0]

            assert null_count == 0, (
                f"Primary key column '{column_name}' in {schema_name}.{table_name} "
                f"contains {null_count} NULL values."
            )

            print(
                f"{schema_name}.{table_name} PK column '{column_name}' has "
                f"{null_count} NULL values."
            )

    cursor.close()
