def interpolation_search(arr, target):
    """
    Perform interpolation search on a sorted list.

    Parameters:
    arr (list): Sorted list of elements to search.
    target: Element to search for.

    Returns:
    int: Index of the target element if found, otherwise -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Example usage:
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 70
result = interpolation_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
