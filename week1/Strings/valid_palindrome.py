"""
Problem: Valid Palindrome (LeetCode #125)
Given a string, determine if it is a palindrome (ignoring non-alphanumeric chars).
"""

def is_palindrome(s: str) -> bool:
    """
    Approach: Two pointers with ASCII checks.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# Test Cases
if __name__ == "__main__":
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome(" ") == True  # Edge case: empty string
    print("All tests passed!")