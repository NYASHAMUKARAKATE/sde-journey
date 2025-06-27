"""
Problem: Given an array of integers, return indices of the two numbers that add up to a target.
Approaches:
  1. Brute Force: O(n²) time, O(1) space
  2. Hashmap: O(n) time, O(n) space (Optimal)
"""

def two_sum_brute(nums: list[int], target: int) -> list[int]:
    """Brute Force: Check all pairs."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_optimal(nums: list[int], target: int) -> list[int]:
    """Optimal: Use a hashmap to store complements."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test Cases
assert two_sum_optimal([2, 7, 11, 15], 9) == [0, 1]
assert two_sum_brute([3, 2, 4], 6) == [1, 2]