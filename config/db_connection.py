import os

import oracledb
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv(), override=True)


def get_connection():
    """
    Creates and returns an Oracle database connection.
    """

    host = os.getenv("HOST")
    port = os.getenv("PORT")
    service = os.getenv("SERVICE_NAME")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    missing = [
        name for name, value in (
            ("HOST", host),
            ("PORT", port),
            ("SERVICE_NAME", service),
            ("USERNAME", username),
            ("PASSWORD", password),
        )
        if not value
    ]
    if missing:
        raise EnvironmentError(
            "Missing database environment variables: " + ", ".join(missing)
        )

    try:
        port = int(port)
    except ValueError as exc:
        raise ValueError("PORT must be an integer") from exc

    dsn = oracledb.makedsn(
        host=host,
        port=port,
        service_name=service,
    )

    try:
        return oracledb.connect(
            user=username,
            password=password,
            dsn=dsn,
        )
    except oracledb.DatabaseError as exc:
        raise ConnectionError(
            f"Oracle connection failed for user '{username}' on service '{service}': {exc}"
        ) from exc