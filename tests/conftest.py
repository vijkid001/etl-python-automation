import os
from datetime import datetime

import pytest
from config.db_connection import get_connection


def pytest_configure(config):
    """Generate a new HTML report for each pytest run."""
    report_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(report_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    report_file = os.path.join(report_dir, f"pytest_report_{timestamp}.html")
    config.option.htmlpath = report_file
    config.option.self_contained_html = True


@pytest.fixture(scope="session")
def db_connection():
    """
    Creates one database connection for the entire test session.
    """
    connection = get_connection()

    yield connection

    connection.close()