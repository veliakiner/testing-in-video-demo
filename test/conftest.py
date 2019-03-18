from src.pogo_log import init_db
import pytest


@pytest.fixture(autouse=True)
def initialise_db():
    init_db()





@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if call.when == "call":
        if rep.outcome == "passed" and hasattr(rep, "wasxfail"):
            # Test passed when it shouldn't've? Make it fail so everyone knows about it!
            rep.outcome = "failed"
    return rep
