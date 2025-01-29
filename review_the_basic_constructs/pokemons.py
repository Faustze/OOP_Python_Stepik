import sys


class MyClass():
    def pokemons(self):
        pokemons = sys.stdin.read().strip().splitlines()
        return len(pokemons) - len(set(pokemons))


m = MyClass()
print(m.pokemons())
