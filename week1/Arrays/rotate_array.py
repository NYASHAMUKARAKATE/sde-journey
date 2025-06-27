"""
Problem: Rotate Array (LeetCode #189)
Given an array, rotate it to the right by k steps.
"""

def rotate(nums: list[int], k: int) -> None:
    """
    Optimal Approach: Reverse trick.
    Time: O(n), Space: O(1)
    """
    k %= len(nums)  # Handle k > array length
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

# Alternative: Brute Force (O(n*k) time)
# def rotate(nums: list[int], k: int) -> None:
#     for _ in range(k):
#         nums.insert(0, nums.pop())

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    rotate(arr, 2)
    assert arr == [4, 5, 1, 2, 3]
    print("All tests passed!")