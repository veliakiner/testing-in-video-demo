from src.pogo_log import add_to_pokedex, list_pokedex
import pytest



def test_add_read():
    # Verify we can add to our Pokedex and read from it
    add_to_pokedex("Bulbasaur", False)
    assert len(list_pokedex()) == 1


@pytest.mark.xfail(reason="A bug with retrieving pokedex")
def test_add_read_multiple():
    add_to_pokedex("Charmander", False)
    add_to_pokedex("Bulbasaur", False)
    assert len(list_pokedex()) == 2


@pytest.mark.xfail(reason="A bug with retrieving pokedex")
def test_add_read_multiple_with_duplicate():
    add_to_pokedex("Bulbasaur", False)
    add_to_pokedex("Squirtle", False)
    add_to_pokedex("Squirtle", False)
    assert len(list_pokedex()) == 2

