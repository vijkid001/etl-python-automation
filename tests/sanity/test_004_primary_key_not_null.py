import os


def test_primary_key_not_null(source_connection, target_connection, etl_config):
    test_data = etl_config["regression_tests"][0]
    source_schema = test_data["source_schema"]
    source_table = test_data["source_table_name"]
    target_schema = test_data["target_schema"]
    target_table = test_data["target_table_name"]

    database_checks = [
        {
            "connection": source_connection,
            "database": os.getenv("SOURCE_CONNECTION", "source_connection"),
            "schema": source_schema,
            "table": source_table,
            "type": "oracle",
        },
        {
            "connection": target_connection,
            "database": os.getenv("TARGET_CONNECTION", "target_connection"),
            "schema": target_schema,
            "table": target_table,
            "type": "postgresql",
        },
    ]

    for check in database_checks:
        schema_name = check["schema"]
        table_name = check["table"]
        db_name = check["database"]
        db_type = os.getenv(f"{db_name}_TYPE", check["type"])

        if check["type"] == "oracle":
            primary_key_query = """
                SELECT c.column_name
                FROM all_constraints cons
                JOIN all_cons_columns c
                    ON cons.owner = c.owner
                   AND cons.constraint_name = c.constraint_name
                WHERE cons.owner = :schema_name
                  AND cons.table_name = :table_name
                  AND cons.constraint_type = 'P'
                ORDER BY c.position
            """
            primary_key_params = {
                "schema_name": schema_name.upper(),
                "table_name": table_name.upper(),
            }
        else:
            primary_key_query = """
                SELECT kcu.column_name
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                    ON tc.constraint_name = kcu.constraint_name
                   AND tc.table_schema = kcu.table_schema
                   AND tc.table_name = kcu.table_name
                WHERE tc.constraint_type = 'PRIMARY KEY'
                  AND tc.table_schema = %s
                  AND tc.table_name = %s
                ORDER BY kcu.ordinal_position
            """
            primary_key_params = (schema_name, table_name)

        print(f"\nDatabase       : {db_name} ({db_type})")
        print(f"Schema         : {schema_name}")
        print(f"Table          : {table_name}")
        print(f"Primary key SQL : {primary_key_query.strip()}")
        cursor = check["connection"].cursor()
        if primary_key_params:
            cursor.execute(primary_key_query, primary_key_params)
        else:
            cursor.execute(primary_key_query)

        primary_key_columns = [row[0] for row in cursor.fetchall()]
        print(f"Primary key columns: {primary_key_columns}")
        assert primary_key_columns, (
            f"{schema_name}.{table_name} does not have a primary key defined."
        )

        for column_name in primary_key_columns:
            if check["type"] == "postgresql":
                null_query = (
                    f'SELECT COUNT(*) FROM "{schema_name}"."{table_name}" '
                    f'WHERE "{column_name}" IS NULL'
                )
            else:
                null_query = (
                    f"SELECT COUNT(*) FROM {schema_name}.{table_name} "
                    f"WHERE {column_name} IS NULL"
                )
            print(f"Null check SQL  : {null_query}")
            cursor.execute(null_query)
            null_count = cursor.fetchone()[0]
            print(f"Null values     : {null_count}")
            assert null_count == 0, (
                f"Primary key column '{column_name}' in {schema_name}.{table_name} "
                f"contains {null_count} NULL values."
            )

        cursor.close()
