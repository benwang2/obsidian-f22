from dataclasses import dataclass
from typing import List

weaknesses = {
    "fire":     ["grass","ice","bug","steel"],
    "water":    ["fire","ground","rock"],
    "electric": ["water","flying"],
    "grass":    ["water","ground","rock"],
    "ice":      ["grass","ground","flying","dragon"],
    "fighting": ["normal","ice","rock","dark","steel"],
    "poison":   ["grass","fairy"],
    "ground":   ["fire","electric","poison","rock","steel"],
    "flying":   ["grass","fighting","bug"],
    "psychic":  ["fighting","poison"],
    "bug":      ["grass","psychic","dark"],
    "rock":     ["fire","ice","flying","bug"],
    "ghost":    ["psychic","ghost"],
    "dragon":   ["dragon"],
    "dark":     ["psychic","ghost"],
    "steel":    ["ice","rock","fairy"],
    "fairy":    ["fighting","dragon","dark"]
}

for w, t in weaknesses.items():
    weaknesses[w] = list(sorted(t))[0]

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

    def get_type_by_weakness(self):
        pass

def count_percent_fire_type_geq_level_n(list_of_pokemon, n):
    num_fire = 0
    num_geq_n = 0

    for pokemon in list_of_pokemon:
        if pokemon.type == 'fire':
            num_fire += 1
            if pokemon.level != "NaN" and float(pokemon.level) >= n:
                num_geq_n += 1

    return round((num_geq_n/num_fire)*100)

def main():
    list_of_pokemon: List[Pokemon] = []
    with open("./data/pokemonTrain.csv","r") as f:
        columns = f.readline()
        for line in f.readlines():
            pokemon = Pokemon(line.strip().split(","))
            list_of_pokemon.append(pokemon)

    p1_1 = count_percent_fire_type_geq_level_n(list_of_pokemon, 40)
    
    with open("./output/pokemon1.txt","w") as f:
        f.write(f"Percentage of fire type pokemon at or above level 40 = {p1_1}")

if __name__ == "__main__":
    main()