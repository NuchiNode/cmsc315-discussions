# Unit 3 Discussion: List Operations

## Overview

For this assignment, I completed the TODO sections in the Python starter file to practice inserting, deleting, and 
searching values in a list. I tested the operations at different positions in the list so I could see how the position 
of an item affects what happens to the other elements.

I used server names for the main examples because that was easier for me to connect to than using random numbers.

## Implementation

I completed three main functions:

- `insert_at()` inserted a value at a specific index.
- `delete_at()` removed and returned a value if the index was valid.
- `search_value()` used a linear search to return the index of a matching value or `-1` if the value was not found.

For insertion, I tested the beginning, middle, and end of the list. Inserting near the beginning caused more existing 
items to shift to the right, while inserting at the end normally did not require the existing items to move.

For deletion, I also tested the beginning, middle, and end. Removing an item caused the values after that position to
shift left and fill the open space.

## Search

I implemented `search_value()` as a linear search using `enumerate()`.

The function checked each value in order until it found a match. If no match was found, the function returned `-1`.

I tested both an existing server and a server that was not in the list.
 
## Edge Cases

I tested several edge cases instead of only testing normal input.

These included:

- Inserting into an empty list
- Deleting an index that did not exist
- Deleting from an empty list
- Searching an empty list
- Searching for a missing value

I also rejected negative indexes in `delete_at()`. Python normally accepts `-1` as the last item in a list, so without 
that check a failed search returning `-1` could accidentally remove the last item.

## Real-World Scenario
The real-world example connects list operations to system administration work. A list can represent servers or open STIG 
findings that need remediation.

A high-priority finding can be inserted near the front, a specific finding can be searched for, and a completed finding 
can be removed from the list.

This also demonstrates why performance matters. Accessing a list by index is fast, but insertion and deletion near the 
beginning or middle can require other items to shift. A linear search may also need to scan the entire list before 
finding a value.


## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

This assignment helped me understand what happens when using Python list operations instead of only using built-in 
methods. I learned why checking indexes matters, particularly because Python accepts negative indexes such as “-1”. One
issue I ran into was accidentally using “list.pop(index)” instead of “lst.pop(index)”. The logic was correct, but I was 
calling “pop()” on the Python “list” type instead of the list passed into the function. The error message helped me 
trace the problem back to that line.

I also tested invalid indexes and empty lists so those cases would return `None` or `-1` instead of causing unexpected 
behavior. List performance depends on the operation. Direct index access is O(1), but inserting or deleting near the 
beginning or middle can be O(N) because all other items must shift. A linear search is also O(N) in the worst case. I 
connected this to managing servers and STIG findings, where the size of the collection and how often it changes can
affect which data structure makes the most sense.