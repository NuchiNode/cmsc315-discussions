"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # Created list stores the values in the stack
        self.elements = []

    def push(self, value):
        # New values are added to the top of the stack
        self.elements.append(value)

    def pop(self):
        # If the stack is empty, return None instead of causing an error.
        # The most recent added value is removed and returned.
        if self.is_empty():
            return None
        return self.elements.pop()

    def peek(self):
        # Returns the top value without removing it from the stack.
        if self.is_empty():
            return None
        return self.elements[-1]

    def is_empty(self):
        # Return True when the stack is empty.
        return len(self.elements) == 0


class Queue:
    def __init__(self):
        # A deque stores the queue values and removes from the front of the queue
        self.elements = deque()

    def enqueue(self, value):
        # New values are added to the back of the queue.
        # Supports FIFO because older values remain at the front.
        self.elements.append(value)

    def dequeue(self):
        # New values are added to the back of the queue.
        # Remove and return an element from the left side of the deque.
        if self.is_empty():
            return None
        return self.elements.popleft()

    def front(self):
        # Returns the first value in the queue without removing it
        # If the queue is empty, return None.
        if self.is_empty():
            return None
        return self.elements[0]

    def is_empty(self):
        # Return True when the queue contains no values.
        return len(self.elements) == 0

def main():
    print("\n=== UNIT 2: STACKS AND QUEUES ===")
    # Add elements or strings to the stack
    stack = Stack()
    stack.push("Login")
    stack.push("Open terminal")
    stack.push("Run update")
    stack.push("Restart service")
    print("Added four elements: Login, Open terminal, Run update, Restart service")

    # peek() reads the top without removing values.
    print("Top element using peek:", stack.peek())

    print("\n==Removed all elements in the stack.==")
    # Each element is popped and printed to console until empty.
    while not stack.is_empty():
        print("Popped:", stack.pop())

    # Popped empty stack.
    # Console returns None if stack is empty
    print("\nPopped from empty stack:", stack.pop())
    # Peeked used on an empty stack.
    # Console returns None if stack is empty
    print("Peeked from empty stack:", stack.peek())

    # Created a new Stack object.
    singleStack = Stack()

    # Added a single item to the Stack object.
    singleStack.push("Second login")
    print("Verified single item added:", singleStack.is_empty())

    # Removed the single element added to the stack.
    singleStack.pop()
    print("Verified single item removed:", singleStack.is_empty())

    print("\n=== QUEUE DEMO ===")

    # Created a queue Object
    queue = Queue()

    # Added four elements to the queue
    queue.enqueue("Ticket 1")
    queue.enqueue("Ticket 2")
    queue.enqueue("Ticket 3")
    queue.enqueue("Ticket 4")

    print("Four tickets were added to the queue: Ticket 1, Ticket 2, Ticket 3, Ticket 4")

    # The front value is the first element added to the queue
    print("The queue front value:",queue.front())

    print("\n==Remove all elements in the queue.==")
    # The first value added should be the first value removed.
    while not queue.is_empty():
        print("Dequeue:", queue.dequeue())

    # Dequeued empty queue.
    # Console returns None if queue is empty
    print("\nDequeued from empty queue:", queue.dequeue())

    # Tested front method on empty queue.
    # Console returns None if queue is empty
    print("Front of empty queue:", queue.front())

    # Created a new queue Object.
    singleQueue = Queue()

    # Added a single item to the Stack object.
    singleQueue.enqueue("Ticket 1A")
    print("Verified single item added:", singleQueue.is_empty())

    # Removed the single element added to the stack.
    singleQueue.dequeue()

    # Verified that the queue is empty.
    print("Verified  single item removed:", singleQueue.is_empty())


if __name__ == "__main__":
    main()
