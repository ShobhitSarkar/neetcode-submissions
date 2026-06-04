'''
- store the values that you've seen in the hashmap
- if encountered, result false 
- if not encountered, add it to the hashmap 
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = {} 

        for num in nums: 
            if num in seen: 
                return True
            else: 
                seen[num] = None 

        return False
        
        