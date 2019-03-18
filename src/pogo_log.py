import sqlite3
from contextlib import contextmanager
import os

conn = sqlite3.connect('log.db')
c = conn.cursor()

@contextmanager
def operate_on_db():
    conn = sqlite3.connect('log.db')
    try:
        yield conn.cursor()
        conn.commit()
    finally:
        conn.close()
try:
    os.remove("log.db")
    with operate_on_db() as c:
        c.execute('''CREATE TABLE Pokedex
                     (dex_number integer, female integer, male integer)''')
except sqlite3.OperationalError:
    pass
SPECIES_TO_POKEDEX = {"Bulbasaur": 1, "Charmander": 4, "Pikachu": 25}
POKEDEX_TO_SPECIES = {SPECIES_TO_POKEDEX[key]: key for key in SPECIES_TO_POKEDEX.keys()}


def add_to_pokedex(species, female):
    pokedex_number = SPECIES_TO_POKEDEX[species]
    with operate_on_db() as c:
        c.execute("""insert into Pokedex
                  values ({}, {}, {})""".format(pokedex_number, int(female), int(not female)))


def list_pokedex():
    with operate_on_db() as c:
        numbers = c.execute("""select distinct dex_number from Pokedex""").fetchall()[:1]
    return [POKEDEX_TO_SPECIES[number[0]] for number in numbers]
#
#
# add_to_pokedex("Bulbasaur", False)
# print(list_pokedex())
