def ternary_search(arr, left, right, target):
    """
    Perform ternary search on a sorted list.

    Parameters:
    arr (list): Sorted list of elements to search.
    left (int): Left index of the subarray to search.
    right (int): Right index of the subarray to search.
    target: Element to search for.

    Returns:
    int: Index of the target element if found, otherwise -1.
    """
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)

    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
result = ternary_search(arr, 0, len(arr) - 1, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
