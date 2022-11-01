# 1
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def filterTemps(fileName, lower=50, upper=60):
    with open(fileName,"r") as f:
        output = []
        for line in f.readlines():
            args = [arg.strip() for arg in line.split(":")]
            date, temp = args

            temp = int(temp)

            if temp >= lower and temp <= upper:
                month_name, date = date.split(" ")
                month = str(months.index(month_name)+1).zfill(2)
                date = date.zfill(2)

                output.append((f"{month}/{date}", temp))

    return output

print(filterTemps('ex.txt', 30, 80))

# 2
from collections import Counter as c

def wordcount(fileName):
    with open(fileName, "r") as f:
        words = []
        for line in f:
            for word in line.split(" "):
                for char in ",.!?":
                    word = word.replace(char,"")
                word = word.replace("\n","")
                if len(word) >= 4 and word.isalpha():
                    words.append(word)
        counted = c(words)
        return list(counted.items())

print(wordcount('ex2.txt'))

# 3
from collections import defaultdict

def classify(wordList):
    output = defaultdict(list)
    for (word, freq) in wordList:
        output[len(word)].append((word,freq))
    
    output = list(sorted(output.items(), key=lambda x: x[0]))
    for i, (length, tuples) in enumerate(output):
        output[i] = (length,list(sorted(tuples)))

    return output

print(classify(wordcount("ex2.txt")))

# 4
print([i+1 for i in range(100) if (i+1)% 4 == 0])

# 5
city_temp = [("EWR", 76), ("HYD", 38),("LAX", 123),("NYC", 12)]
print([city[0] for city in city_temp if city[1] > 70])

# 6
print([y+l for y in "FSJE" for l in "RC"])

# 7
print([(i,j) for i in range(1, 10) for j in range(i, 11) if (i+j)%3 == 0])