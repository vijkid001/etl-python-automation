
###################### 5.0  #######################################
from pathlib import Path
import json
import os
from datetime import datetime

import pytest

from config.db_connection import get_oracle_connection, get_postgres_connection


DATA_FILE_PATH = Path(__file__).parent / "data" / "etl_test_data.json"


@pytest.fixture(scope="session")
def etl_config():
    """Load the central test data file once per test session."""
    with open(DATA_FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def get_suite_data(suite_name: str):
    """Load a specific section from the shared JSON file."""
    with open(DATA_FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get(suite_name, [])


def create_connection(connection_name):
    connection_type = os.getenv(f"{connection_name}_TYPE")
    assert connection_type, f"{connection_name}_TYPE is not set in .env"

    if connection_type.lower() == "oracle":
        return get_oracle_connection(connection_name)
    if connection_type.lower() in {"postgres", "postgresql"}:
        return get_postgres_connection(connection_name)
    raise ValueError(f"Unsupported database type: {connection_type}")


@pytest.fixture
def source_connection():
    connection_name = os.getenv("SOURCE_CONNECTION")
    assert connection_name, "SOURCE_CONNECTION is not set in .env"
    connection = create_connection(connection_name)
    yield connection
    connection.close()


@pytest.fixture
def target_connection():
    connection_name = os.getenv("TARGET_CONNECTION")
    assert connection_name, "TARGET_CONNECTION is not set in .env"
    connection = create_connection(connection_name)
    yield connection
    connection.close()


@pytest.fixture
def oracle_db(source_connection):
    return source_connection


@pytest.fixture
def postgres_db(target_connection):
    return target_connection


def pytest_configure(config):
    """Generate a new HTML report for each pytest run."""
    report_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(report_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    report_file = os.path.join(report_dir, f"pytest_report_{timestamp}.html")
    config.option.htmlpath = report_file
    config.option.self_contained_html = True


###################### 5.0  #######################################

###################### 4.0  #######################################

# import os  # Loads Python's operating system tool to read environment settings
# import pytest  # Loads the testing framework to manage test setup and cleanup
# from config.db_connection import get_oracle_connection, get_postgres_connection  # Imports database connector functions
# from datetime import datetime #For Reporting

# def create_connection(connection_name):  # Helper function that builds a connection based on a named config
#     """Create a database connection based on the connection definition in .env."""
#     assert connection_name, "Connection name is not set."  # Validates that a connection name was provided
#     connection_type = os.getenv(f"{connection_name}_TYPE")  # Reads the database type (e.g., "oracle") from .env
#     assert connection_type, f"{connection_name}_TYPE is not set in .env"  # Validates that the database type exists in .env

#     if connection_type.lower() == "oracle":  # Checks if the database is Oracle
#         return get_oracle_connection(connection_name)  # Creates and returns an Oracle connection
#     elif connection_type.lower() == "postgresql":  # Checks if the database is PostgreSQL
#         return get_postgres_connection(connection_name)  # Creates and returns a PostgreSQL connection
#     else:  # Handles any unrecognized database types
#         raise ValueError(f"Unsupported database type: {connection_type}")  # Stops execution and reports an unsupported database error


# @pytest.fixture  # Marks this function as an automated test setup/cleanup helper
# def source_connection():  # Defines the test fixture for the source database
#     connection_name = os.getenv("SOURCE_CONNECTION")  # Fetches the active source database name from .env
#     assert connection_name, "SOURCE_CONNECTION is not set in .env"  # Validates that SOURCE_CONNECTION is defined in .env
#     connection = create_connection(connection_name)  # Opens the connection to the source database
#     yield connection  # Hands the active connection to the test and waits for it to finish
#     connection.close()  # Safely closes the source connection after the test completes


# @pytest.fixture  # Marks this function as an automated test setup/cleanup helper
# def target_connection():  # Defines the test fixture for the target database
#     connection_name = os.getenv("TARGET_CONNECTION")  # Fetches the active target database name from .env
#     assert connection_name, "TARGET_CONNECTION is not set in .env"  # Validates that TARGET_CONNECTION is defined in .env
#     connection = create_connection(connection_name)  # Opens the connection to the target database
#     yield connection  # Hands the active connection to the test and waits for it to finish
#     connection.close()  # Safely closes the target connection after the test completes


# ####REPORTING############

# def pytest_configure(config):
#     """Generate a new HTML report for each pytest run."""
#     report_dir = os.path.join(os.getcwd(), "reports")
#     os.makedirs(report_dir, exist_ok=True)

#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
#     report_file = os.path.join(report_dir, f"pytest_report_{timestamp}.html")
#     config.option.htmlpath = report_file
#     config.option.self_contained_html = True

###################### 4.0  #######################################
###################### 3.0  #######################################

# import os  # Loads Python's operating system tool to read environment settings

# import pytest  # Loads the testing framework to manage test setup and cleanup

# from config.db_connection import (  # Imports the database connector functions from your config module
#     get_oracle_connection,  # Function to connect to Oracle databases
#     get_postgres_connection,  # Function to connect to PostgreSQL databases
# )


# def create_connection(
#     connection_name,
# ):  # Helper function that builds a connection based on a named config
#     """
#     Create a database connection based on the connection
#     definition in .env.
#     """

#     assert (
#         connection_name
#     ), "Connection name is not set."  # Validates that a connection name was provided

#     connection_type = os.getenv(
#         f"{connection_name}_TYPE"
#     )  # Reads the database type (e.g., "oracle") from .env

#     assert (
#         connection_type
#     ), f"{connection_name}_TYPE is not set in .env"  # Validates that the database type exists in .env

#     if connection_type.lower() == "oracle":  # Checks if the database is Oracle

#         return get_oracle_connection(
#             connection_name
#         )  # Creates and returns an Oracle connection

#     elif (
#         connection_type.lower() == "postgresql"
#     ):  # Checks if the database is PostgreSQL

#         return get_postgres_connection(
#             connection_name
#         )  # Creates and returns a PostgreSQL connection

#     else:  # Handles any unrecognized database types

#         raise ValueError(  # Stops execution and reports an unsupported database error
#             f"Unsupported database type: {connection_type}"
#         )


# @pytest.fixture  # Marks this function as an automated test setup/cleanup helper
# def source_connection():  # Defines the test fixture for the source database

#     connection_name = os.getenv(
#         "SOURCE_CONNECTION"
#     )  # Fetches the active source database name from .env

#     assert (
#         connection_name
#     ), "SOURCE_CONNECTION is not set in .env"  # Validates that SOURCE_CONNECTION is defined in .env

#     connection = create_connection(
#         connection_name
#     )  # Opens the connection to the source database

#     yield connection  # Hands the active connection to the test and waits for it to finish

#     connection.close()  # Safely closes the source connection after the test completes


# @pytest.fixture  # Marks this function as an automated test setup/cleanup helper
# def target_connection():  # Defines the test fixture for the target database

#     connection_name = os.getenv(
#         "TARGET_CONNECTION"
#     )  # Fetches the active target database name from .env

#     assert (
#         connection_name
#     ), "TARGET_CONNECTION is not set in .env"  # Validates that TARGET_CONNECTION is defined in .env

#     connection = create_connection(
#         connection_name
#     )  # Opens the connection to the target database

#     yield connection  # Hands the active connection to the test and waits for it to finish

#     connection.close()  # Safely closes the target connection after the test completes

###################### 3.0  #######################################

###################### 2.0  #######################################
# import os

# import pytest

# from config.db_connection import (
#     get_oracle_connection,
#     get_postgres_connection
# )


# def create_connection(connection_name):
#     """
#     Create a database connection based on the connection
#     definition in .env.
#     """

#     assert connection_name, "Connection name is not set."

#     connection_type = os.getenv(f"{connection_name}_TYPE")

#     assert connection_type, (
#         f"{connection_name}_TYPE is not set in .env"
#     )

#     if connection_type.lower() == "oracle":

#         return get_oracle_connection(connection_name)

#     elif connection_type.lower() == "postgresql":

#         return get_postgres_connection(connection_name)

#     else:

#         raise ValueError(
#             f"Unsupported database type: {connection_type}"
#         )


# @pytest.fixture
# def source_connection():

#     connection_name = os.getenv("SOURCE_CONNECTION")

#     assert connection_name, (
#         "SOURCE_CONNECTION is not set in .env"
#     )

#     connection = create_connection(connection_name)

#     yield connection

#     connection.close()


# @pytest.fixture
# def target_connection():

#     connection_name = os.getenv("TARGET_CONNECTION")

#     assert connection_name, (
#         "TARGET_CONNECTION is not set in .env"
#     )

#     connection = create_connection(connection_name)

#     yield connection

#     connection.close()


# # 2.0 Working
# import os

# import pytest

# from config.db_connection import get_oracle_connection


# @pytest.fixture
# def source_connection():
#     """
#     Creates a connection to the configured source database.
#     """

#     connection_name = os.getenv("SOURCE_CONNECTION")

#     assert connection_name, "SOURCE_CONNECTION is not set in .env"

#     connection = get_oracle_connection(connection_name)

#     yield connection

#     connection.close()

###################### 2.0  #######################################

######################## 1.0 ##############################################
# import os


# import pytest
# from config.db_connection import get_connection


# def pytest_configure(config):
#     """Generate a new HTML report for each pytest run."""
#     report_dir = os.path.join(os.getcwd(), "reports")
#     os.makedirs(report_dir, exist_ok=True)

#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
#     report_file = os.path.join(report_dir, f"pytest_report_{timestamp}.html")
#     config.option.htmlpath = report_file
#     config.option.self_contained_html = True


# @pytest.fixture(scope="session")
# def db_connection():
#     """
#     Creates one database connection for the entire test session.
#     """
#     connection = get_connection()

#     yield connection

#     connection.close()

########################1.0##############################################