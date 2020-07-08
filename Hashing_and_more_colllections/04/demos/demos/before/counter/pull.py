import csv

from collections import Counter

with open('../data/Male_WorldCupPlayers.csv', 'r', encoding='utf8') as players:
    reader = csv.reader(players)
    next(reader) #skip column names
    name_list = []
    for row in reader:
        name_list.append(row[6])
    print(name_list)
    