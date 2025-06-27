"""
Problem: Reverse a singly linked list.
Approaches:
  1. Iterative: O(n) time, O(1) space (Optimal)
  2. Recursive: O(n) time, O(n) space (call stack)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list_iterative(head: ListNode) -> ListNode:
    """Optimal: Three pointers (prev, curr, next)."""
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

def reverse_list_recursive(head: ListNode) -> ListNode:
    """Recursive: Reverse rest of the list, then adjust head."""
    if not head or not head.next:
        return head
    p = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return p

# Test Cases
def list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

head = ListNode(1, ListNode(2, ListNode(3)))
assert list_to_array(reverse_list_iterative(head)) == [3, 2, 1]