# Sorting Algorithms
Sorting techniques are algorithms used to arrange elements of a list or array in a particular order, usually in ascending or descending order. Here are some of the most common sorting techniques:

1. **Bubble Sort**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

2. **Selection Sort**: Divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted. It repeatedly selects the smallest (or largest) element from the unsorted sublist, swaps it with the first unsorted element, and moves the sublist boundary one element to the right.

3. **Insertion Sort**: Builds the final sorted list one item at a time, with the input elements being taken one by one and inserted in their correct position in the already sorted part of the list.

4. **Merge Sort**: A divide-and-conquer algorithm that divides the unsorted list into n sublists, each containing one element, and then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining.

5. **Quick Sort**: Another divide-and-conquer algorithm that selects a 'pivot' element from the array and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. It then recursively sorts the sub-arrays.

6. **Heap Sort**: Converts the list into a heap, a binary tree where the parent node is always greater than or equal to (or less than or equal to) the child nodes. The largest (or smallest) element is removed from the heap, and the heap is restructured, repeating this process until the heap is empty and the list is sorted.

7. **Radix Sort**: A non-comparative sorting algorithm that sorts numbers by processing individual digits. It processes the least significant digit first (or the most significant digit first, depending on the implementation) and uses a stable sort (like counting sort) as a subroutine.

8. **Counting Sort**: A non-comparative sorting algorithm that counts the occurrences of each unique element and then calculates the position of each element in the sorted output.

In addition to the basic implementations of sorting algorithms, Python provides several built-in functions and features that enhance sorting capabilities. These features can make sorting operations more efficient and versatile.

## Built-in Sorting Functions

1. **`sorted()` function**: This function returns a new sorted list from the elements of any iterable.
2. **`list.sort()` method**: This method sorts the list in place and returns `None`.

### Additional Features

1. **Custom Key Functions**: Both `sorted()` and `list.sort()` accept a `key` parameter, which allows you to provide a function that extracts a comparison key from each list element.

2. **Reverse Sorting**: Both `sorted()` and `list.sort()` accept a `reverse` parameter, which allows you to sort in descending order.

3. **Stability**: Python's sorting algorithms are stable, meaning that when multiple records have the same key, their original order is preserved in the sorted output.

Here are some examples demonstrating these additional features:

### Custom Key Functions

```python
# Sorting a list of tuples by the second element
data = [(1, 2), (3, 1), (5, 4), (2, 3)]
sorted_data = sorted(data, key=lambda x: x[1])
print("Sorted by second element:", sorted_data)

# Sorting a list of strings by length
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=len)
print("Sorted by length:", sorted_words)
```

### Reverse Sorting

```python
# Sorting a list in descending order
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers, reverse=True)
print("Sorted in descending order:", sorted_numbers)

# In-place sorting in descending order
numbers.sort(reverse=True)
print("In-place sorted in descending order:", numbers)
```

### Stability

```python
# Sorting by the first element, then by the second element (stable sort)
data = [(2, 'B'), (1, 'A'), (2, 'A'), (1, 'B')]
sorted_data = sorted(data, key=lambda x: (x[0], x[1]))
print("Stable sort by multiple keys:", sorted_data)
```

### Using `attrgetter` and `itemgetter` from `operator` module

For more complex key functions, especially when sorting objects, you can use `attrgetter` and `itemgetter` from the `operator` module.

```python
from operator import itemgetter, attrgetter

# Sorting a list of dictionaries by a specific key
data = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}, {'name': 'Dave', 'age': 32}]
sorted_data = sorted(data, key=itemgetter('age'))
print("Sorted by age:", sorted_data)

# Sorting a list of objects by a specific attribute
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person('John', 25), Person('Jane', 22), Person('Dave', 32)]
sorted_people = sorted(people, key=attrgetter('age'))
print("Sorted by age:", [(person.name, person.age) for person in sorted_people])
```

## Summary

- **`sorted(iterable, key=None, reverse=False)`**: Returns a new sorted list from the elements of any iterable.
- **`list.sort(key=None, reverse=False)`**: Sorts the list in place and returns `None`.
- **`key` parameter**: A function that serves as a key for the sort comparison.
- **`reverse` parameter**: A boolean value. If `True`, the list elements are sorted as if each comparison were reversed.
- **Stability**: Maintains the relative order of records with equal keys.
