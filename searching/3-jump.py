import math

def jump_search(arr, target):
    """
    Perform jump search on a sorted list.

    Parameters:
    arr (list): Sorted list of elements to search.
    target: Element to search for.

    Returns:
    int: Index of the target element if found, otherwise -1.
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
result = jump_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
