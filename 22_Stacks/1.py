# STACKS: linear data structure
 
# works on the LIFO principle.
# elements can be added or removed from the same end.

# Functions associated: 
# insert -> pop() 
# delete -> pop() 
# empty() -> returns True for an empty stack 
# size() -> gives the length/size of stack 
# top() -> gives reference of last element in stack

#  Can be implemented using LISTS, QUEUE, and COLLECTIONS


# Implementation of Stacks using List:

stack = []
stack.append("Raj")
stack.append("40")
stack.append("Aryan")
print(stack)

print(stack.pop())
print(stack)


# Implementation of Stacks using Collection.deque:
# append and pop operations are faster in deque as compared to lists, rest is same

from collections import deque
stack1 = deque()
stack.append("Raaajj")
print(stack.pop())
print(stack1)


# Implementation of Stacks using Queue:
# put() -> for insertion
# get() -> for removal 
# maxsize() -> used to put maximum number of items allowed in queue
# full() -> returns True for a full queue
# put(x) -> used to insert x in queue
# qsize() -> gives the size of queue

from queue import LifoQueue
stack2 = LifoQueue(maxsize=4)
stack2.put("My name is ")
stack2.put("Raj")
# print(stack2)          LifoQueue doesn't allow printing the stack. for it just use a simple list for stacks.
print(stack2.get())
print(stack2.qsize())

#  we can look through the elements in a LifoQueue using the destructive way, i.e.
from queue import LifoQueue

stack = LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)

while not stack.empty():
    print(stack.get())


# to use a non-destructive way, there is a HACK
from queue import LifoQueue

stack = LifoQueue()

stack.put(1)
stack.put(2)
stack.put(3)

# Peek into the stack (not officially documented, but works)
print(list(stack.queue))  # Output: [1, 2, 3]
