from collections import deque

#to use deque like a Stack (LIFO)
#use the pop/append methods from one side only

d = deque()

print('deque\'s right side as a stack - append/pop')
d.append(1)
d.append(2)
d.append(3)
print(d)
#remove from the same side that append was called from
d.pop()
print(d)
d.pop()
print(d)
d.pop()
print(d)



print('deque\'s left side as a stack - appendleft/popleft')
d.appendleft(1)
d.appendleft(2)
d.appendleft(3)
print(d)
#remove from the same side that append was called from
d.popleft()
print(d)
d.popleft()
print(d)
d.popleft()
print(d)
