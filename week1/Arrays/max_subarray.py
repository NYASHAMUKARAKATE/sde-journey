"""
Problem: Find the contiguous subarray with the largest sum.
Approaches:
  1. Kadane's Algorithm: O(n) time, O(1) space (Optimal)
  2. Brute Force: O(n²) time, O(1) space
"""

def max_subarray_kadane(nums: list[int]) -> int:
    """Optimal: Track max current and global sums."""
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    return max_global

def max_subarray_brute(nums: list[int]) -> int:
    """Brute Force: Check all subarrays."""
    max_sum = float('-inf')
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    return max_sum

# Test Cases
assert max_subarray_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6