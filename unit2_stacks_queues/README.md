# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO): Using last-in, first-out
- Queue (FIFO): Using first-in, first-out

## Implementation
I implemented the Stack using a Python list. The push() method 
added values to the top of the stack, pop() removed the most 
recently added value, and peek() returned the top value without removing it.
I implemented the Queue using collections.deque. The enqueue() method added
values to the back of the queue, dequeue() removed values from the front, and 
front() returned the first value without removing it.

## Testing and Edge Cases
I tested both structures with four values to demonstrate LIFO and FIFO behavior. 
I also tested pop() and peek() on an empty stack and dequeue() and front() on an 
empty queue. These methods returned None instead of causing an error. I created 
single-item stack and queue tests and verified that each structure became empty 
after its only item was removed.