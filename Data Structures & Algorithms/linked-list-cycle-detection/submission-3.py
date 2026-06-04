'''
Floyd's algoritm: 
- init two pointers - slow and fast 
- move the slow pointer one at a time 
- move the fast pointer 2 at a time 
- if at any point, they both point to the same node -> then cyclic 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head 
        fast = head 

        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast: 
                return True 

        return False
        