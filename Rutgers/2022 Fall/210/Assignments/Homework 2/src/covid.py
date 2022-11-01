from collections import defaultdict
import csv
import re

def part1(data):
    for entry in data:
        if "-" in entry["age"]:
            lower, upper = [float(num) for num in entry["age"].split("-")]
            entry["age"] = f"{round((lower+upper)/2,0):.0f}"

def part2(data):
    date_patt = re.compile(r"(\d+)\.(\d+)\.(\d+)")
    for entry in data:
        for col in ("date_onset_symptoms","date_admission_hospital","date_confirmation"):
            entry[col] = date_patt.sub(r"\2.\1.\3",entry[col])

def part3(data):
    provinces_lat = defaultdict(defaultdict)
    provinces_lon = defaultdict(defaultdict)
    for entry in data:
        province = entry["province"]
        if entry["latitude"] != "NaN":
            provinces_lat[province]["count"] = provinces_lat[province].get("count",0)+1
            provinces_lat[province]["value"] = provinces_lat[province].get("value",0)+float(entry["latitude"])
        if entry["longitude"] != "NaN":
            provinces_lon[province]["count"] = provinces_lon[province].get("count",0)+1
            provinces_lon[province]["value"] = provinces_lon[province].get("value",0)+float(entry["longitude"])
            
        
    for entry in data:
        province = entry["province"]
        if entry["latitude"] == "NaN":
            entry["latitude"] = str(round(provinces_lat[province]["value"]/provinces_lat[province]["count"],2))
        if entry["longitude"] == "NaN":
            entry["longitude"] = str(round(provinces_lon[province]["value"]/provinces_lon[province]["count"],2))

def part4(data):
    cities_by_province = defaultdict(list)

    for entry in data:
        province, city = entry["province"], entry["city"]
        if city != "NaN":
            cities_by_province[province].append(city)
    
    city_freq = defaultdict(dict)
    for (province, cities) in cities_by_province.items():
        freq = {city: cities.count(city) for city in set(cities)} # frequency map cities
        sorted_by_freq = {k:v for (k,v) in sorted(freq.items(), key=lambda x: x[1], reverse=True)} # sort by num occurrences
        
        max_freq = max(sorted_by_freq.values())
        common = list(filter(lambda x: x[1] == max_freq, sorted_by_freq.items()))
        city_freq[province] = sorted(common, key=lambda x:x[0])[0][0]

    for entry in data:
        if entry["city"] == "NaN":
            entry["city"] = city_freq[entry["province"]]

def part5(data):
    symptoms_by_province = defaultdict(dict)

    for entry in data:
        province = entry["province"]
        if entry["symptoms"] != "NaN":
            symptoms = [s.strip() for s in entry["symptoms"].split(";")]
            for symptom in symptoms:
                symptoms_by_province[province][symptom] = symptoms_by_province[province].get(symptom, 0)+1

    for (province, symptoms) in symptoms_by_province.items():
        freq = {k:v for (k,v) in sorted(symptoms.items(), key=lambda x:x[1],reverse=True)}
        max_freq = max(freq.values())
        most_common = list(filter(lambda x: x[1] == max_freq, freq.items()))
        symptoms_by_province[province] = sorted(most_common, key=lambda x:x[0])[0][0]

    for entry in data:
        if entry["symptoms"] == "NaN":
            entry["symptoms"] = symptoms_by_province[entry["province"]]

def main():
    with open("covidTrain.csv","r") as f:
        covidTrain = [
            row for row in csv.DictReader(f)
        ]
    
    part1(covidTrain)
    part2(covidTrain)
    part3(covidTrain)
    part4(covidTrain)
    part5(covidTrain)

    with open("covidResult.csv","w") as f:
        f.write(",".join([key for key in covidTrain[0].keys()])+"\n")
        for entry in covidTrain:
            f.write(",".join(entry.values())+"\n")

if __name__ == "__main__":
    main()