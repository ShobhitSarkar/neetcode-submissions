'''
keep track of element - hashmap/dict or something 

iterate through the array: 
    - if the num exists in the dict: then return True 
    - if not -> add it to the hashmap 

caveat: 
    - the first element needs to be added separately 

edge cases: 
    - list has 0 elements
    - return False 


'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0: 
            return False 
        
        if (len(nums) == 2) and (nums[0] == nums[1]): 
            return True 
        
        seen = {} ## keep track of seen elements 

        for num in nums: 
            if num in seen: 
                return True 
            else: 
                seen[num] = None 

        
        return False