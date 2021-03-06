from src.pogo_log import add_to_pokedex, list_pokedex, present_in_pokedex
import pytest
from test.lib import xfail
import pytest
import flaky

def test_add_read():
    # Verify we can add to our Pokedex and read from it
    add_to_pokedex("Bulbasaur", False)
    assert len(list_pokedex()) == 1

@pytest.mark.xfail(reason="Bug with list_pokedex") # xfail a test is going to fail
def test_add_read_multiple():
    add_to_pokedex("Charmander", False)
    add_to_pokedex("Bulbasaur", False)
    assert len(list_pokedex()) == 2


def test_add_read_multiple_with_duplicate():
    add_to_pokedex("Bulbasaur", False)
    add_to_pokedex("Squirtle", False)
    add_to_pokedex("Squirtle", False)
    with xfail(AssertionError, "bug with list_pokedex"): # only raise an xfail if failure happens at expected point in code
        assert len(list_pokedex()) == 2


@flaky.flaky(max_runs=4, min_passes=2)
def test_present_in_dex():
    # Make a test pass that fails sometimes
    add_to_pokedex("Bulbasaur", True)
    assert present_in_pokedex("Bulbasaur", True)
