import csv
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    first_name: str
    last_name: str


def load_people():
    people = []
    with open('../data/randomnames.csv', 'r') as names:
        names_reader = csv.reader(names, delimiter= ' ')
        for row in names_reader:
            people.append(Person(row[0], row[1]))
    return people