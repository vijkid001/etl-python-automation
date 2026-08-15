import os


def test_aggregate_validation(db_connection):

    source_schema = os.getenv("SOURCE_SCHEMA")
    target_schema = os.getenv("TARGET_SCHEMA")

    assert source_schema, "SOURCE_SCHEMA is not set in .env"
    assert target_schema, "TARGET_SCHEMA is not set in .env"

    cursor = db_connection.cursor()

    # ---------------------------------------------------------
    # 1. Calculate expected aggregation from SOURCE
    # ---------------------------------------------------------

    cursor.execute(f"""
        SELECT
            PRODUCT,
            REGION,
            SUM(QUANTITY) AS TOTAL_QUANTITY,
            SUM(AMOUNT) AS TOTAL_AMOUNT
        FROM {source_schema}.SALES_SRC
        GROUP BY PRODUCT, REGION
        ORDER BY PRODUCT, REGION
    """)

    source_rows = cursor.fetchall()

    # ---------------------------------------------------------
    # 2. Get actual aggregation from TARGET
    # ---------------------------------------------------------

    cursor.execute(f"""
        SELECT
            PRODUCT,
            REGION,
            TOTAL_QUANTITY,
            TOTAL_AMOUNT
        FROM {target_schema}.SALES_SUMMARY_TGT
        ORDER BY PRODUCT, REGION
    """)

    target_rows = cursor.fetchall()

    cursor.close()

    # ---------------------------------------------------------
    # 3. Display results
    # ---------------------------------------------------------

    print(f"\nSource aggregated rows : {len(source_rows)}")
    print(f"Target rows             : {len(target_rows)}")

    # ---------------------------------------------------------
    # 4. Compare row counts
    # ---------------------------------------------------------

    assert len(source_rows) == len(target_rows), (
        f"Aggregated row count mismatch. "
        f"Source={len(source_rows)}, Target={len(target_rows)}"
    )

    # ---------------------------------------------------------
    # 5. Compare actual data
    # ---------------------------------------------------------

    mismatches = []

    for source_row, target_row in zip(source_rows, target_rows):

        if source_row != target_row:
            mismatches.append(
                {
                    "source": source_row,
                    "target": target_row
                }
            )

    # ---------------------------------------------------------
    # 6. Fail if any aggregation differs
    # ---------------------------------------------------------

    assert not mismatches, (
        f"Aggregate validation failed.\n"
        f"Mismatches: {mismatches}"
    )