from dataclasses import dataclass
from re import L
from typing import Dict, List

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

    def __repr__(self):
        # id,name,level,personality,type,weakness,atk,def,hp,stage
        return f"{self.id},{self.name},{self.level},{self.personality},{self.type},{self.weakness},{self.atk},{self.defense},{self.hp},{self.stage}"

def count_percent_fire_type_geq_level_n(list_of_pokemon: List[Pokemon], n):
    num_fire = 0
    num_geq_n = 0

    for pokemon in list_of_pokemon:
        if pokemon.type == 'fire':
            num_fire += 1
            if pokemon.level != "NaN" and float(pokemon.level) >= n:
                num_geq_n += 1

    return round((num_geq_n/num_fire)*100)

def part1(list_of_pokemon):
    result = count_percent_fire_type_geq_level_n(list_of_pokemon,40)
    with open("./output/pokemon1.txt","w") as f:
        f.write(f"Percentage of fire type pokemon at or above level 40 = {result}")

def get_weakness_mapping(list_of_pokemon: List[Pokemon]):
    freq: Dict[Dict[str]] = {}
    for i, pokemon in enumerate(list_of_pokemon):
        if pokemon.type != "NaN":
            if pokemon.weakness not in freq:
                freq[pokemon.weakness] = {}
            freq[pokemon.weakness][pokemon.type] = freq[pokemon.weakness].get(pokemon.type, 0)+1
    
    most_common = {}

    for (ptype,weak_to) in freq.items():
        sorted_by_freq = sorted(weak_to.items(),key=lambda x: x[1],reverse=True)
        max_occurences = sorted_by_freq[0][1]

        max_occ_only = [i for i in sorted_by_freq if i[1] == max_occurences]

        mode_types = sorted(max_occ_only,key=lambda x: x[0])

        most_common[ptype] = mode_types[0][0]

    return most_common

def part2(list_of_pokemon):
    weakness_map = get_weakness_mapping(list_of_pokemon)
    for pokemon in list_of_pokemon:
        if pokemon.type == "NaN":
            pokemon.type = weakness_map[pokemon.weakness]

def main():
    list_of_pokemon: List[Pokemon] = []
    with open("./data/pokemonTrain.csv","r") as f:
        columns = f.readline().split(",")
        for line in f.readlines():
            pokemon = Pokemon(line.strip().split(","))
            list_of_pokemon.append(pokemon)

    part1(list_of_pokemon)
    part2(list_of_pokemon)

if __name__ == "__main__":
    main()