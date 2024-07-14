def fibonacci_search(arr, target):
    """
    Perform fibonacci search on a sorted list.

    Parameters:
    arr (list): Sorted list of elements to search.
    target: Element to search for.

    Returns:
    int: Index of the target element if found, otherwise -1.
    """
    n = len(arr)
    fib2 = 0
    fib1 = 1
    fibM = fib1 + fib2

    while fibM < n:
        fib2 = fib1
        fib1 = fibM
        fibM = fib1 + fib2

    offset = -1

    while fibM > 1:
        i = min(offset + fib2, n - 1)
        if arr[i] < target:
            fibM = fib1
            fib1 = fib2
            fib2 = fibM - fib1
            offset = i
        elif arr[i] > target:
            fibM = fib2
            fib1 = fib1 - fib2
            fib2 = fibM - fib1
        else:
            return i

    if fib1 and arr[offset + 1] == target:
        return offset + 1

    return -1

# Example usage:
arr = [1, 3, 7, 15, 19, 24, 31, 36, 42, 47]
target = 24
result = fibonacci_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
