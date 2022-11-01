from collections import defaultdict

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

    def __repr__(self):
        # id,name,level,personality,type,weakness,atk,def,hp,stage
        return f"{self.id},{self.name},{self.level},{self.personality},{self.type},{self.weakness},{self.atk},{self.defense},{self.hp},{self.stage}"

def count_percent_fire_type_geq_level_n(list_of_pokemon, n):
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
    with open("./pokemon1.txt","w") as f:
        f.write(f"Percentage of fire type pokemon at or above level 40 = {result}")

def get_weakness_mapping(list_of_pokemon):
    freq = {}
    for pokemon in list_of_pokemon:
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

def get_avg_stats(list_of_pokemon):
    atk_values = [float(pokemon.atk) for pokemon in list_of_pokemon if pokemon.atk != "NaN"]
    def_values = [float(pokemon.defense) for pokemon in list_of_pokemon if pokemon.defense != "NaN"]
    hp_values = [float(pokemon.hp) for pokemon in list_of_pokemon if pokemon.hp != "NaN"]

    return {
        "atk":  sum(atk_values)/len(atk_values),
        "def":  sum(def_values)/len(def_values),
        "hp":   sum(hp_values)/len(hp_values),
    }

def part2(list_of_pokemon):
    weakness_map = get_weakness_mapping(list_of_pokemon)
    for pokemon in list_of_pokemon:
        if pokemon.type == "NaN":
            pokemon.type = weakness_map[pokemon.weakness]

def part3(list_of_pokemon):
    group1 = [pokemon for pokemon in list_of_pokemon if pokemon.level > 40]

    g1_avgstats = get_avg_stats(group1)

    group2 = [pokemon for pokemon in list_of_pokemon if pokemon.level <= 40]
    g2_avgstats = get_avg_stats(group2)

    for pokemon in list_of_pokemon:
        if "NaN" not in (pokemon.atk,pokemon.defense, pokemon.hp): continue
        updated_stats = {}
        if pokemon.level > 40:
            updated_stats = g1_avgstats
        else:
            updated_stats = g2_avgstats

        if pokemon.atk == 'NaN':
            pokemon.atk = round(updated_stats['atk'],1)
        if pokemon.defense == 'NaN':
            pokemon.defense = round(updated_stats['def'],1)
        if pokemon.hp == 'NaN':
            pokemon.hp = round(updated_stats['hp'],1)

def part4(list_of_pokemon):
    type_to_personality = defaultdict(set)

    for pokemon in list_of_pokemon:
        type_to_personality[pokemon.type].add(pokemon.personality)

    for p_type, values in type_to_personality.items():
        type_to_personality[p_type] = sorted(values)

    with open("./pokemon4.txt","w") as f:
        for p_type in (sorted(type_to_personality,key=lambda x: x[0])):
            f.write(f'{p_type}: {", ".join(type_to_personality[p_type])}\n')

def part5(list_of_pokemon):
    hp_for_stage3 = [float(pokemon.hp) for pokemon in list_of_pokemon if pokemon.stage == "3.0"]
    avg_hp = round(sum(hp_for_stage3)/len(hp_for_stage3),0)

    with open("./pokemon5.txt","w") as f:
        f.write(f"Average hit point for pokemon of stage 3.0 = {avg_hp:.0f}")

def main():
    list_of_pokemon = []
    with open("./pokemonTrain.csv","r") as f:
        columns = f.readline()
        for line in f.readlines():
            pokemon = Pokemon(line.strip().split(","))
            list_of_pokemon.append(pokemon)

    part1(list_of_pokemon)
    part2(list_of_pokemon)
    part3(list_of_pokemon)

    with open("./pokemonResult.csv", "w") as f:
        f.write(columns)
        f.writelines([ repr(p)+"\n" for p in list_of_pokemon])

    part4(list_of_pokemon)
    part5(list_of_pokemon)


if __name__ == "__main__":
    main()