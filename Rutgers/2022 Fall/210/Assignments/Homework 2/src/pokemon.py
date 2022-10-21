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
        self.level = float(self.level)

    def repr(self):
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

    group1 = [pokemon for pokemon in list_of_pokemon if pokemon.level > 40 and "NaN" not in (pokemon.atk,pokemon.defense, pokemon.hp)]
    group1_avg = {}

    for pokemon in group1:
        group1_avg["atk"] = group1_avg.get("atk",0) + float(pokemon.atk)
        group1_avg["defense"] = group1_avg.get("defense",0) + float(pokemon.defense)
        group1_avg["hp"] = group1_avg.get("hp",0) + float(pokemon.hp)

    print(group1_avg)

    for key in group1_avg:
        group1_avg[key] = round(group1_avg[key]/len(group1),1)

    print(group1_avg)
    group2 = [pokemon for pokemon in list_of_pokemon if pokemon.level <= 40 and "nan" not in (pokemon.atk,pokemon.defense, pokemon.hp)]
    group2_avg = {}
    
    for pokemon in group2:
        group2_avg["atk"] = group2_avg.get("atk",0) + float(pokemon.atk)
        group2_avg["defense"] = group2_avg.get("defense",0) + float(pokemon.defense)
        group2_avg["hp"] = group2_avg.get("hp",0) + float(pokemon.hp)

    print(group2_avg)

    for key in group2_avg:
        group2_avg[key] = round(group2_avg[key]/len(group2),1)

    print(group2_avg)

    for pokemon in list_of_pokemon:
        if "NaN" not in (pokemon.atk,pokemon.defense, pokemon.hp): continue
        updated_stats = {}
        if pokemon.level > 40:
            updated_stats = group1_avg
        else:
            updated_stats = group2_avg

        if pokemon.atk == 'NaN':
            pokemon.atk = updated_stats['atk']
        if pokemon.defense == 'NaN':
            pokemon.defense = updated_stats['defense']
        if pokemon.hp == 'NaN':
            pokemon.hp = updated_stats['hp']

    with open("./output/pokemonResult.csv", "w") as f:
        f.writelines([ p.repr()+"\n" for p in list_of_pokemon])


def main():
    list_of_pokemon: List[Pokemon] = []
    with open("./data/pokemonTrain.csv","r") as f:
        columns = f.readline()
        for line in f.readlines():
            pokemon = Pokemon(line.strip().split(","))
            list_of_pokemon.append(pokemon)

    part1(list_of_pokemon)
    part2(list_of_pokemon)

if __name__ == "__main__":
    main()