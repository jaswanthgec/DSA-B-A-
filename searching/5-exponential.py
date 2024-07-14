def binary_search_recursive(arr, left, right, target):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, left, mid - 1, target)
        else:
            return binary_search_recursive(arr, mid + 1, right, target)
    return -1

def exponential_search(arr, target):
    """
    Perform exponential search on a sorted list.

    Parameters:
    arr (list): Sorted list of elements to search.
    target: Element to search for.

    Returns:
    int: Index of the target element if found, otherwise -1.
    """
    if arr[0] == target:
        return 0

    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    return binary_search_recursive(arr, i // 2, min(i, n - 1), target)

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 11
result = exponential_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
