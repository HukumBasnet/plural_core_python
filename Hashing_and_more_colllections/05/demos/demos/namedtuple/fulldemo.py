import csv


#turn csv into list of tuples
data = open('../data/randomnames.csv', 'r')
names = [n for n in csv.reader(data)]
people_raw_tuple = [t for t in map(tuple, names)]
print(names)
print(people_raw_tuple)
person_raw_tuple = people_raw_tuple[0]
print(person_raw_tuple)
import inspect
print(inspect.getmro(type(person_raw_tuple)))

print(person_raw_tuple[0])
print(person_raw_tuple[1])
from collections.abc import Sequence
print(isinstance(person_raw_tuple, Sequence))
for a in person_raw_tuple: print(a)
#use named tuple 
from collections import namedtuple
Person = namedtuple('Person','first_name last_name')
print(inspect.getmro(Person))
person_named_tuple = Person('Jon','Flanders')
print(person_named_tuple.first_name)
print(person_named_tuple.last_name)
print(isinstance(person_named_tuple, Sequence))
for a in person_named_tuple: print(a)
people_named_tuple = [p for p in map(Person._make, names)]
person_named_tuple = people_named_tuple[0]
print(person_named_tuple)
print(person_raw_tuple)
print(person_named_tuple == person_raw_tuple)
#create typing.NamedTuple
from models import NamedTuplePerson
print(inspect.getmro(NamedTuplePerson))
person_typing_named_tuple = NamedTuplePerson('Jon', 'Flanders')
print(person_typing_named_tuple)
print(person_typing_named_tuple.first_name)
print(person_typing_named_tuple.last_name)
print(isinstance(person_typing_named_tuple, Sequence))
for a in person_typing_named_tuple: print(a)
people_typing_named_tuple = [p for p in map(NamedTuplePerson._make, names)]
print(people_typing_named_tuple)
person_typing_named_tuple = people_typing_named_tuple[0]
print(person_raw_tuple)
print(person_raw_tuple == person_typing_named_tuple)
print(person_named_tuple)
print(people_named_tuple == person_typing_named_tuple)