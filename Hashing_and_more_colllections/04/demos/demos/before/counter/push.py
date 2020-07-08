import random

from collections import Counter

from game import simulate_game
from models import Person, load_people

people = load_people()
print(people)
