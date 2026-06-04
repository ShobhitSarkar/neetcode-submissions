# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
- get all the elements of the linked list -> store in array 

- iterate through array in reverse order: 
    - create new head node 
    - create new linkedlist node for each value 
    - append to the previous node 
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head 
        nums = [] 

        while temp != None: 
            nums.append(temp.val)
            temp = temp.next 
        

        new_head = ListNode()
        new_temp = new_head

        for i in range(len(nums) -1, -1, -1): 
            new_node = ListNode(nums[i])
            new_temp.next = new_node
            new_temp = new_temp.next 
        
        return new_head.next
        
        