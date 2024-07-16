# Sorting 
Sorting techniques are algorithms used to arrange elements of a list or array in a particular order, usually in ascending or descending order. Here are some of the most common sorting techniques:

1. **Bubble Sort**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.

2. **Selection Sort**: Divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining to be sorted. It repeatedly selects the smallest (or largest) element from the unsorted sublist, swaps it with the first unsorted element, and moves the sublist boundary one element to the right.

3. **Insertion Sort**: Builds the final sorted list one item at a time, with the input elements being taken one by one and inserted in their correct position in the already sorted part of the list.

4. **Merge Sort**: A divide-and-conquer algorithm that divides the unsorted list into n sublists, each containing one element, and then repeatedly merges sublists to produce new sorted sublists until there is only one sublist remaining.

5. **Quick Sort**: Another divide-and-conquer algorithm that selects a 'pivot' element from the array and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. It then recursively sorts the sub-arrays.

6. **Heap Sort**: Converts the list into a heap, a binary tree where the parent node is always greater than or equal to (or less than or equal to) the child nodes. The largest (or smallest) element is removed from the heap, and the heap is restructured, repeating this process until the heap is empty and the list is sorted.

7. **Radix Sort**: A non-comparative sorting algorithm that sorts numbers by processing individual digits. It processes the least significant digit first (or the most significant digit first, depending on the implementation) and uses a stable sort (like counting sort) as a subroutine.

8. **Counting Sort**: A non-comparative sorting algorithm that counts the occurrences of each unique element and then calculates the position of each element in the sorted output.
