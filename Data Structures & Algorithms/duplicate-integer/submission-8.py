'''
- we have to keep track of seen elements
    - init a hashmap to keep track of elements
- one approach: 
    - store all the elements with their frequencies 
    - iterate through the hashmap and then see if any of the frequences is > 1 
- another approach: 
    - if not in hashmap -> add it 
    - if element encountered and then it's in hashmap -> return true 

- edge cases: 
    - length of list is 0 
    - length of the list is 1 
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0: 
            return False 
        
        if len(nums) == 1: 
            return False 

        seen = {}
        seen[nums[0]] = None

        for i in range(1, len(nums)): 
            if nums[i] in seen: 
                return True
            else: 
                seen[nums[i]] = None 
        
        return False
        