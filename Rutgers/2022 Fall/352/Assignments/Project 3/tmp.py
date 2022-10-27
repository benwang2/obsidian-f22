# 1
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def filterTemps(fileName, lower=50, upper=60):
    with open(fileName,"r") as f:
        output = []
        for line in f.readlines():
            args = [arg.strip() for arg in line.split(":")]
            date, temp = args

            temp = int(temp)

            if temp >= lower and temp <= 60:
                month_name, date = date.split(" ")
                month = str(months.index(month_name)+1).zfill(2)
                date = date.zfill(2)

                output.append((f"{month}/{date}", temp))

    return output

# 2
from collections import Counter as c

def wordcount(fileName):
    with open(fileName, "r") as f:
        words = []
        for word in f.read().split(" "):
            word = word.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
            if len(word) >= 4 and word.isalpha():
                pass