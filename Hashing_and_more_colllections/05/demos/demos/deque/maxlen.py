from collections import deque

d = deque(maxlen=5)
d.extendleft([i for i in range(0,5)])
print(d)
d.append(5)

print('going over maxlen by adding to right side - discards on left side')
print(d)

d.appendleft(6)
print('going over maxlen by adding to left side -  discards on the right side')
print(d)