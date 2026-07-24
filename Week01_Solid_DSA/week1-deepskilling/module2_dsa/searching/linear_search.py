"""
Searching Algorithm: Linear Search
-------------------------------------
Checks every element one by one until the target is found or the list
is exhausted.

Time Complexity : O(n) worst/average case, O(1) best case
Space Complexity: O(1)
Works on: sorted or unsorted lists.
"""

from typing import List


def linear_search(arr: List[int], target: int) -> int:
    """Returns the index of target in arr, or -1 if not found."""
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    data = [4, 2, 7, 1, 9, 5]

    print(f"Searching for 9: index {linear_search(data, 9)}")
    print(f"Searching for 100: index {linear_search(data, 100)}")

    assert linear_search(data, 9) == 4
    assert linear_search(data, 4) == 0
    assert linear_search(data, 100) == -1
    assert linear_search([], 1) == -1
    print("All linear search checks passed.")
