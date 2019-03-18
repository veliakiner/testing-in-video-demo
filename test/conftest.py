from src.pogo_log import init_db
import pytest


@pytest.fixture(autouse=True)
def initialise_db():
    init_db()
