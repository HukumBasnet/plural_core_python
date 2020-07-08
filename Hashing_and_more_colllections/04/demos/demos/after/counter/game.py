import random

def simulate_game(people):
    for p in people:
        #assign a random score between 1 and 10
        people[p] += random.randint(1, 10)
    return