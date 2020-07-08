from collections import Counter
from collections import OrderedDict

from game import simulate_game
from models import Person, load_people

people = load_people()
game = Counter({person: 0 for person in people})
simulate_game(game)
top_ten = game.most_common(10)
print(top_ten)
by_name = OrderedDict(sorted(top_ten, key= lambda p:p[0].last_name))
print(by_name)