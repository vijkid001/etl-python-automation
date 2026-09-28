
import os  # Standard library module to read operating system environment variables
import oracledb  # Python driver library for connecting to Oracle databases
import psycopg  # Python driver library for connecting to PostgreSQL databases
from dotenv import load_dotenv  # Function to load environment variables from a local .env file

load_dotenv()  # Reads the .env file and populates environment settings


def get_oracle_connection(connection_name):  # Function to create an Oracle database connection using dynamic prefixes
    """Create an Oracle database connection using .env."""
    host = os.getenv(f"{connection_name}_HOST")  # Fetches Oracle host address from .env
    port = os.getenv(f"{connection_name}_PORT")  # Fetches Oracle port number from .env
    service_name = os.getenv(f"{connection_name}_SERVICE_NAME")  # Fetches Oracle service name from .env
    username = os.getenv(f"{connection_name}_USERNAME")  # Fetches Oracle username from .env
    password = os.getenv(f"{connection_name}_PASSWORD")  # Fetches Oracle password from .env

    assert host, f"{connection_name}_HOST is not set in .env"  # Validates host value exists
    assert port, f"{connection_name}_PORT is not set in .env"  # Validates port value exists
    assert service_name, f"{connection_name}_SERVICE_NAME is not set in .env"  # Validates service name exists
    assert username, f"{connection_name}_USERNAME is not set in .env"  # Validates username exists
    assert password, f"{connection_name}_PASSWORD is not set in .env"  # Validates password exists

    dsn = oracledb.makedsn(host=host, port=int(port), service_name=service_name)  # Constructs Data Source Name (DSN) string
    return oracledb.connect(user=username, password=password, dsn=dsn)  # Establishes and returns live Oracle connection


def get_postgres_connection(connection_name):  # Function to create a PostgreSQL connection using dynamic prefixes
    """Create a PostgreSQL database connection using .env."""
    host = os.getenv(f"{connection_name}_HOST")  # Fetches PostgreSQL host address from .env
    port = os.getenv(f"{connection_name}_PORT")  # Fetches PostgreSQL port number from .env
    database = os.getenv(f"{connection_name}_DATABASE")  # Fetches PostgreSQL database name from .env
    username = os.getenv(f"{connection_name}_USERNAME")  # Fetches PostgreSQL username from .env
    password = os.getenv(f"{connection_name}_PASSWORD")  # Fetches PostgreSQL password from .env

    assert host, f"{connection_name}_HOST is not set in .env"  # Validates host value exists
    assert port, f"{connection_name}_PORT is not set in .env"  # Validates port value exists
    assert database, f"{connection_name}_DATABASE is not set in .env"  # Validates database name exists
    assert username, f"{connection_name}_USERNAME is not set in .env"  # Validates username exists
    assert password, f"{connection_name}_PASSWORD is not set in .env"  # Validates password exists

    return psycopg.connect(host=host, port=int(port), dbname=database, user=username, password=password)  # Establishes and returns live PostgreSQL connection

##################################################

# import os  # Standard library module to read operating system environment variables

# import oracledb  # Python driver library for connecting to Oracle databases
# import psycopg  # Python driver library for connecting to PostgreSQL databases
# from dotenv import (
#     load_dotenv,  # Function to load environment variables from a local .env file
# )


# load_dotenv()  # Reads the .env file and populates environment settings


# def get_oracle_connection(
#     connection_name,
# ):  # Function to create an Oracle database connection using dynamic prefixes
#     """
#     Create an Oracle database connection using .env.
#     """

#     host = os.getenv(
#         f"{connection_name}_HOST"
#     )  # Fetches Oracle host address from .env (e.g., SOURCE_HOST)
#     port = os.getenv(
#         f"{connection_name}_PORT"
#     )  # Fetches Oracle port number from .env
#     service_name = os.getenv(
#         f"{connection_name}_SERVICE_NAME"
#     )  # Fetches Oracle service name from .env
#     username = os.getenv(
#         f"{connection_name}_USERNAME"
#     )  # Fetches Oracle username from .env
#     password = os.getenv(
#         f"{connection_name}_PASSWORD"
#     )  # Fetches Oracle password from .env

#     assert (
#         host
#     ), f"{connection_name}_HOST is not set in .env"  # Validates host value exists
#     assert (
#         port
#     ), f"{connection_name}_PORT is not set in .env"  # Validates port value exists
#     assert (
#         service_name
#     ), f"{connection_name}_SERVICE_NAME is not set in .env"  # Validates service name exists
#     assert (
#         username
#     ), f"{connection_name}_USERNAME is not set in .env"  # Validates username exists
#     assert (
#         password
#     ), f"{connection_name}_PASSWORD is not set in .env"  # Validates password exists

#     dsn = oracledb.makedsn(  # Constructs the Data Source Name (DSN) string required by Oracle
#         host=host,  # Passes Oracle host address
#         port=int(
#             port
#         ),  # Converts port string to integer required by oracledb
#         service_name=service_name,  # Passes Oracle database service name
#     )

#     return oracledb.connect(  # Establishes and returns an active Oracle connection object
#         user=username,  # Passes database user
#         password=password,  # Passes user password
#         dsn=dsn,  # Passes constructed DSN string
#     )


# def get_postgres_connection(
#     connection_name,
# ):  # Function to create a PostgreSQL connection using dynamic prefixes
#     """
#     Create a PostgreSQL database connection using .env.
#     """

#     host = os.getenv(
#         f"{connection_name}_HOST"
#     )  # Fetches PostgreSQL host address from .env
#     port = os.getenv(
#         f"{connection_name}_PORT"
#     )  # Fetches PostgreSQL port number from .env
#     database = os.getenv(
#         f"{connection_name}_DATABASE"
#     )  # Fetches PostgreSQL database name from .env
#     username = os.getenv(
#         f"{connection_name}_USERNAME"
#     )  # Fetches PostgreSQL username from .env
#     password = os.getenv(
#         f"{connection_name}_PASSWORD"
#     )  # Fetches PostgreSQL password from .env

#     assert (
#         host
#     ), f"{connection_name}_HOST is not set in .env"  # Validates host value exists
#     assert (
#         port
#     ), f"{connection_name}_PORT is not set in .env"  # Validates port value exists
#     assert (
#         database
#     ), f"{connection_name}_DATABASE is not set in .env"  # Validates database name exists
#     assert (
#         username
#     ), f"{connection_name}_USERNAME is not set in .env"  # Validates username exists
#     assert (
#         password
#     ), f"{connection_name}_PASSWORD is not set in .env"  # Validates password exists

#     return psycopg.connect(  # Establishes and returns an active PostgreSQL connection object
#         host=host,  # Passes PostgreSQL host address
#         port=int(
#             port
#         ),  # Converts port string to integer required by psycopg
#         dbname=database,  # Passes target database name
#         user=username,  # Passes database user
#         password=password,  # Passes user password
#     )

###################################################################

# import os

# import oracledb
# import psycopg
# from dotenv import load_dotenv


# load_dotenv()


# def get_oracle_connection(connection_name):
#     """
#     Create an Oracle database connection using .env.
#     """

#     host = os.getenv(f"{connection_name}_HOST")
#     port = os.getenv(f"{connection_name}_PORT")
#     service_name = os.getenv(f"{connection_name}_SERVICE_NAME")
#     username = os.getenv(f"{connection_name}_USERNAME")
#     password = os.getenv(f"{connection_name}_PASSWORD")

#     assert host, f"{connection_name}_HOST is not set in .env"
#     assert port, f"{connection_name}_PORT is not set in .env"
#     assert service_name, f"{connection_name}_SERVICE_NAME is not set in .env"
#     assert username, f"{connection_name}_USERNAME is not set in .env"
#     assert password, f"{connection_name}_PASSWORD is not set in .env"

#     dsn = oracledb.makedsn(
#         host=host,
#         port=int(port),
#         service_name=service_name
#     )

#     return oracledb.connect(
#         user=username,
#         password=password,
#         dsn=dsn
#     )


# def get_postgres_connection(connection_name):
#     """
#     Create a PostgreSQL database connection using .env.
#     """

#     host = os.getenv(f"{connection_name}_HOST")
#     port = os.getenv(f"{connection_name}_PORT")
#     database = os.getenv(f"{connection_name}_DATABASE")
#     username = os.getenv(f"{connection_name}_USERNAME")
#     password = os.getenv(f"{connection_name}_PASSWORD")

#     assert host, f"{connection_name}_HOST is not set in .env"
#     assert port, f"{connection_name}_PORT is not set in .env"
#     assert database, f"{connection_name}_DATABASE is not set in .env"
#     assert username, f"{connection_name}_USERNAME is not set in .env"
#     assert password, f"{connection_name}_PASSWORD is not set in .env"

#     return psycopg.connect(
#         host=host,
#         port=int(port),
#         dbname=database,
#         user=username,
#         password=password
#     )


# 2.0
# import os

# import oracledb
# from dotenv import load_dotenv


# load_dotenv()


# def get_oracle_connection(connection_name):
#     """
#     Create an Oracle database connection using the
#     connection configuration from .env.

#     Example:
#         get_oracle_connection("ORACLE1")
#     """

#     host = os.getenv(f"{connection_name}_HOST")
#     port = os.getenv(f"{connection_name}_PORT")
#     service_name = os.getenv(f"{connection_name}_SERVICE_NAME")
#     username = os.getenv(f"{connection_name}_USERNAME")
#     password = os.getenv(f"{connection_name}_PASSWORD")

#     assert host, f"{connection_name}_HOST is not set in .env"
#     assert port, f"{connection_name}_PORT is not set in .env"
#     assert service_name, f"{connection_name}_SERVICE_NAME is not set in .env"
#     assert username, f"{connection_name}_USERNAME is not set in .env"
#     assert password, f"{connection_name}_PASSWORD is not set in .env"

#     dsn = oracledb.makedsn(
#         host=host,
#         port=int(port),
#         service_name=service_name
#     )

#     connection = oracledb.connect(
#         user=username,
#         password=password,
#         dsn=dsn
#     )

#     return connection


# import os
# import oracledb
# from dotenv import find_dotenv, load_dotenv

# load_dotenv(find_dotenv(), override=True)


# def get_connection():
#     """
#     Creates and returns an Oracle database connection.
#     """

#     host = os.getenv("HOST")
#     port = os.getenv("PORT")
#     service = os.getenv("SERVICE_NAME")
#     username = os.getenv("USERNAME")
#     password = os.getenv("PASSWORD")

#     missing = [
#         name for name, value in (
#             ("HOST", host),
#             ("PORT", port),
#             ("SERVICE_NAME", service),
#             ("USERNAME", username),
#             ("PASSWORD", password),
#         )
#         if not value
#     ]
#     if missing:
#         raise EnvironmentError(
#             "Missing database environment variables: " + ", ".join(missing)
#         )

#     try:
#         port = int(port)
#     except ValueError as exc:
#         raise ValueError("PORT must be an integer") from exc

#     dsn = oracledb.makedsn(
#         host=host,
#         port=port,
#         service_name=service,
#     )

#     try:
#         return oracledb.connect(
#             user=username,
#             password=password,
#             dsn=dsn,
#         )
#     except oracledb.DatabaseError as exc:
#         raise ConnectionError(
#             f"Oracle connection failed for user '{username}' on service '{service}': {exc}"
#         ) from exc
