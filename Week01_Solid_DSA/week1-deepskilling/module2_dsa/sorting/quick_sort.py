"""
Sorting Algorithm: Quick Sort
--------------------------------
A divide-and-conquer algorithm. Picks a 'pivot' element, partitions the
array so smaller elements go left and larger go right, then recursively
sorts each partition.

Time Complexity : O(n log n) average, O(n^2) worst case (rare, with a
                  bad pivot choice on already-sorted/reverse data)
Space Complexity: O(log n) average due to recursion stack
"""

from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_in_place(arr: List[int], low: int = 0, high: int = None) -> List[int]:
    """In-place (Lomuto partition) version - O(1) extra space besides
    the recursion stack."""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = _partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)
    return arr


def _partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print(f"Original: {data}")
    print(f"Sorted (functional): {quick_sort(data)}")
    print(f"Sorted (in-place):   {quick_sort_in_place(data.copy())}")

    assert quick_sort(data) == sorted(data)
    assert quick_sort_in_place(data.copy()) == sorted(data)
    assert quick_sort([]) == []
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    print("All quick sort checks passed.")
