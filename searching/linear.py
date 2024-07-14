def linear_search(arr, target):
    """
    Perform linear search on a list.

    Parameters:
    arr (list): List of elements to search.
    target: Element to search for.

    Returns:
    int: Index of the target element if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

arr = [3, 5, 2, 4, 9]
target = 4
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")