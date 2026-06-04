class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0: 
            return False 

        store = {} 

        for num in nums: 
            if num in store: 
                return True 
            else: 
                store[num] = False 

        return False
        