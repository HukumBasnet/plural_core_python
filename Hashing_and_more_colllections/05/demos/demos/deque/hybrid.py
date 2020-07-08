from collections import deque

virtual_queue = deque()
#add items from left to right
#put customers in a virtual queue
virtual_queue.extendleft([f'Person{i}' for i in range(0,11)])
print(virtual_queue)
#normally we'd use pop to use the deque like a queue
#when it is time for a customer to go into the room
#our business rules however allow a VIP to be able to jump to the front
#of the current queue
important_person = 'Person100'
#since deque allows us to append to the right side at the same time
virtual_queue.append(important_person)
print(virtual_queue)
#deque allows us to keep the left to right addition for non-VIP customers
#but allows use to add from the right enabling us to implement this
#pattern easily
