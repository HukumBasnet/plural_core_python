from collections import deque

#to use deque like a queue always pop from the opposite side
#that append  was called on
print('deque as a queue - right to left')
d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)
#take an item from the left
d.popleft()
#1 was added first so it comes out first
print(d)
d.popleft()
print(d)
d.popleft()
print(d)
print('deque as a queue - left to right')
#if you use appendleft then pop will give you queue semantics
d.appendleft(1)
d.appendleft(2)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.pop()
print(d)
d.pop()
print(d)