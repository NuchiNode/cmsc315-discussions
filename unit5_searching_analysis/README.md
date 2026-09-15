# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

## Reflection

This assignment taught me how linear and binary search locate values differently and how sorting data can make searching
more efficient. Linear search checks each value from the beginning until the target is found, which gives it O(n) time 
complexity in the worst case. Binary search uses the low, high, and middle indexes to repeatedly reduce a sorted search 
area by half, giving it O(log n) time complexity. I also learned that the choice between linear and binary search 
depends on the type of data and the search functionality a programmer wants to implement.

One challenge I had was understanding how the low and high indexes changed during binary search. I updated the low index
when the middle value was greater than the target instead of updating the high index. Testing the algorithm 
with a small, sorted dataset helped me see which direction the search needed to move.

Linear search would be useful for small or unsorted datasets because no sorting is required, and modern hardware can 
process smaller collections quickly. Binary search would be better for a large, already sorted dataset, such as server 
IDs that are searched repeatedly. The trade-off is that binary search is faster, but the data must remain sorted.
