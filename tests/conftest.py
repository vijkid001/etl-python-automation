import pytest
from config.db_connection import get_connection


@pytest.fixture(scope="session")
def db_connection():
    """
    Creates one database connection for the entire test session.
    """
    connection = get_connection()

    yield connection

    connection.close()