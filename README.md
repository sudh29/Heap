# Heap

readme_content = """
# Python heapq Module

Python's `heapq` module provides functions to create and manipulate heaps. Heaps are binary trees for which every parent node has a value less than or equal to any of its children. This makes it suitable for applications such as priority queues and sorting algorithms.

## Methods

### Heap Creation:

1. **heapify(heap)**:
   - Converts a list into a heap in-place.
   - Time Complexity: O(n), where n is the number of elements in the list.

2. **heappush(heap, item)**:
   - Pushes a new element onto the heap while maintaining the heap invariant.
   - Time Complexity: O(log n), where n is the number of elements in the heap.

3. **heappop(heap)**:
   - Removes and returns the smallest element from the heap.
   - Time Complexity: O(log n), where n is the number of elements in the heap.

4. **heappushpop(heap, item)**:
   - Pushes a new element onto the heap and then pops and returns the smallest element.
   - Equivalent to calling `heappush()` followed by `heappop()`, but more efficient.
   - Time Complexity: O(log n), where n is the number of elements in the heap.

5. **heapreplace(heap, item)**:
   - Pops and returns the smallest element from the heap, then pushes a new element onto the heap.
   - More efficient than calling `heappop()` followed by `heappush()`.
   - Time Complexity: O(log n), where n is the number of elements in the heap.

### Heap Access:

6. **heappushpop(heap, item)**:
   - Returns the smallest element from the heap without removing it.
   - Time Complexity: O(1).

7. **nlargest(n, iterable)**:
   - Returns the n largest elements from the iterable.
   - Time Complexity: O(n + k log n), where n is the length of the iterable and k is the number of elements returned.

8. **nsmallest(n, iterable)**:
   - Returns the n smallest elements from the iterable.
   - Time Complexity: O(n + k log n), where n is the length of the iterable and k is the number of elements returned.

### Miscellaneous:

9. **merge(*iterables, key=None, reverse=False)**:
   - Merges multiple sorted inputs into a single sorted output.
   - Time Complexity: O(n log k), where n is the total number of elements and k is the number of input iterables.

10. **_heapify_max(heap)**:
    - Custom method to convert a list into a max-heap in-place.
    - Utilizes `heapify()` and negates values in the list to simulate a max-heap.
"""

