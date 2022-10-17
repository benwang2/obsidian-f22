from dataclasses import dataclass
from typing import List

@dataclass()
class Pokemon:
    id: int
    name: str
    level: int
    personality: str
    type: str
    weakness: str
    atk: int
    defense: int
    hp: int
    stage:int

    def __init__(self, args):
        self.id,self.name,self.level,self.personality,self.type,self.weakness,self.atk,self.defense,self.hp,self.stage = args

        self.id = int(float(self.id))
        self.level = int(float(self.level))
        self.atk = int(float(self.atk))
        self.defense = int(float(self.defense))
        self.hp = int(float(self.hp))
        self.stage = int(float(self.stage))

def count_percent_fire_type_geq_level_n(list_of_pokemon, n):
    num_fire = 0
    num_geq_n = 0

    for pokemon in list_of_pokemon:
        if pokemon.type == 'fire':
            num_fire += 1
            if pokemon.level >= n:
                num_geq_n += 1

    return num_geq_n/num_fire


def main():
    list_of_pokemon: List[Pokemon] = []
    with open("./data/pokemonTrain.csv","r") as f:
        columns = f.readline()
        for line in f.readlines():
            pokemon = Pokemon(line.strip().split(","))
            list_of_pokemon.append(pokemon)

    p1_1 = count_percent_fire_type_geq_level_n(list_of_pokemon, 40)
    print(p1_1)

if __name__ == "__main__":
    main()