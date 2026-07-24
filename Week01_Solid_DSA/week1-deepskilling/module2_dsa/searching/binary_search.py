"""
Searching Algorithm: Binary Search
-------------------------------------
Repeatedly divides a SORTED array's search interval in half, comparing
the target against the middle element.

Time Complexity : O(log n)
Space Complexity: O(1) iterative, O(log n) recursive (call stack)
Precondition    : array MUST be sorted.
"""

from typing import List


def binary_search_iterative(arr: List[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr: List[int], target: int, low: int = 0, high: int = None) -> int:
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


if __name__ == "__main__":
    sorted_data = [1, 3, 5, 7, 9, 11, 13, 15]

    print(f"Iterative search for 7: index {binary_search_iterative(sorted_data, 7)}")
    print(f"Recursive search for 15: index {binary_search_recursive(sorted_data, 15)}")
    print(f"Search for 4 (not present): index {binary_search_iterative(sorted_data, 4)}")

    assert binary_search_iterative(sorted_data, 7) == 3
    assert binary_search_iterative(sorted_data, 1) == 0
    assert binary_search_iterative(sorted_data, 15) == 7
    assert binary_search_iterative(sorted_data, 4) == -1

    assert binary_search_recursive(sorted_data, 7) == 3
    assert binary_search_recursive(sorted_data, 4) == -1
    print("All binary search checks passed.")
