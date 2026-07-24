"""
Sorting Algorithm: Merge Sort
--------------------------------
A divide-and-conquer algorithm. Recursively splits the array into
halves until each sub-array has one element, then merges the sub-arrays
back together in sorted order.

Time Complexity : O(n log n) in ALL cases (best, average, worst) -
                  its main advantage over Quick Sort's worst case.
Space Complexity: O(n) - requires extra space for merging.
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return _merge(left_half, right_half)


def _merge(left: List[int], right: List[int]) -> List[int]:
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    sorted_data = merge_sort(data)
    print(f"Original: {data}")
    print(f"Sorted:   {sorted_data}")

    assert sorted_data == sorted(data)
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    print("All merge sort checks passed.")
