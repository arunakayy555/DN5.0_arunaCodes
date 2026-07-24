"""
Sorting Algorithm: Bubble Sort
---------------------------------
Repeatedly steps through the list, compares adjacent elements, and
swaps them if they're in the wrong order. Simple but inefficient on
large lists.

Time Complexity : O(n^2) worst/average, O(n) best (already sorted, with
                  early-exit optimization)
Space Complexity: O(1) - in-place
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    result = arr.copy()
    n = len(result)
    for i in range(n):
        swapped = False
        # After each pass, the largest remaining element "bubbles up"
        # to its correct position at the end, so we shrink the range.
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break  # already sorted, no need to keep looping
    return result


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data = bubble_sort(data)
    print(f"Original: {data}")
    print(f"Sorted:   {sorted_data}")

    assert sorted_data == sorted(data)
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    print("All bubble sort checks passed.")
