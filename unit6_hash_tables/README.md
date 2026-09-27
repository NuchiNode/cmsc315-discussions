# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

While completing this assignment, I used server IDs as the keys and operating systems as the values because this is 
similar to how I might keep track of systems in an IT environment. I practiced adding entries to the dictionary, looking
up values using their key, updating existing values, and deleting entries.

One challenge was understanding how the key locates a value in the dictionary. Testing the program with a small set of 
server IDs helped me see how each key is linked to a specific value. I also learned that trying to access a key that 
does not exist causes a KeyError. To handle this, I used get() and pop() with default values, which return a message 
instead of an error.

A dictionary is a hash table because Python hashes each key to determine where its key-value pair is stored. A collision
happens when two different keys map to the same location. Python handles these collisions internally by finding another 
open spot. Hash tables improve efficiency because searching, inserting, updating, and deleting are O(1) on average.
