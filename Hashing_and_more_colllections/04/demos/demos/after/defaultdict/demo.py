import csv

from collections import defaultdict

with open('../data/Male_WorldCupPlayers.csv', 'r', encoding='utf8') as players:
    reader = csv.reader(players)
    next(reader) #skip column names
    name_list = []
    for row in reader:
        name_list.append((row[2],row[6]))
    print(name_list)
    players_by_country = defaultdict(list)
    for item in name_list:
        players_by_country[item[0]].append(item[1])
    print(players_by_country)
  