'''
- init a slow, fast pointer 
- move the fast pointer n steps 
- now move the fast and slow pointer together, till the fast reaches 
the end 
    - at this point, the slow pointer is at the n-1 th position from the end 
- change the pointers 
- return the list 
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        for i in range(n + 1): 
            fast = fast.next 

        while fast:
            slow = slow.next
            fast = fast.next 

        slow.next = slow.next.next

        return dummy.next

        