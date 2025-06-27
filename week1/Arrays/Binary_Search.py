"""
Problem: Given a sorted array, return the index of a target element (or -1 if not found).
Approaches:
  1. Iterative Binary Search: O(log n) time, O(1) space (Optimal)
  2. Linear Search: O(n) time, O(1) space
"""

def binary_search(nums: list[int], target: int) -> int:
    """Optimal: Divide and conquer using mid-point comparison."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def linear_search(nums: list[int], target: int) -> int:
    """Brute Force: Check every element."""
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1

# Test Cases
assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
assert linear_search([-1, 0, 3, 5, 9, 12], 2) == -1