"""
Problem: Find the length of the longest substring without repeating characters.
Approach: Sliding Window with Hashmap. O(n) time, O(min(m, n)) space.
"""

def longest_substring(s: str) -> int:
    seen = {}
    max_len = left = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# Test Cases
assert longest_substring("abcabcbb") == 3
assert longest_substring("bbbbb") == 1