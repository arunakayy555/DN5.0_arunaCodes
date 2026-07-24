"""
Data Structures: Arrays
--------------------------
Covers array traversal, in-memory representation, and basic time
complexity intuition for common operations.

Time complexity cheat-sheet for Python lists (dynamic arrays):
    Index access        -> O(1)
    Append              -> O(1) amortized
    Insert at position   -> O(n)
    Delete at position   -> O(n)
    Search (unsorted)    -> O(n)
"""

from typing import List


def traverse_array(arr: List[int]) -> None:
    """O(n) traversal - visits every element exactly once."""
    for index, value in enumerate(arr):
        print(f"Index {index}: {value}")


def find_max(arr: List[int]) -> int:
    """O(n) - single pass to find the maximum element."""
    if not arr:
        raise ValueError("Array is empty")
    max_val = arr[0]
    for value in arr[1:]:
        if value > max_val:
            max_val = value
    return max_val


def reverse_array(arr: List[int]) -> List[int]:
    """O(n) - two-pointer in-place reversal (returns a new list here
    for easy testing, but the swap logic is what matters)."""
    result = arr.copy()
    left, right = 0, len(result) - 1
    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    return result


def rotate_array(arr: List[int], k: int) -> List[int]:
    """O(n) - rotate array to the right by k positions."""
    if not arr:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k] if k else arr.copy()


def remove_duplicates(arr: List[int]) -> List[int]:
    """O(n) - remove duplicates while preserving order, using a set to
    track what's already been seen (O(1) average lookup)."""
    seen = set()
    result = []
    for value in arr:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


if __name__ == "__main__":
    sample = [5, 3, 8, 1, 9, 2]

    print("Original array:")
    traverse_array(sample)

    print(f"\nMax value: {find_max(sample)}")
    print(f"Reversed: {reverse_array(sample)}")
    print(f"Rotated by 2: {rotate_array(sample, 2)}")
    print(f"Deduplicated [1,2,2,3,1]: {remove_duplicates([1, 2, 2, 3, 1])}")

    assert find_max(sample) == 9
    assert reverse_array(sample) == [2, 9, 1, 8, 3, 5]
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    print("\nAll array operation checks passed.")
