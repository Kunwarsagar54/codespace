import csv

with open("favourite.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[1])