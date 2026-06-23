"""
-- high level algorithm 

- init pointers: 
    - low = first index of the array 
    - high = last index of the array 
- start iterating: 
    - calculate a middle index 
    - if the nums of middle index is target, return it 
    - if the nums is lesser, then target is on right side 
        - set low to middle + 1
    - if the nums is higher, target is on the left side 
        - set high to middle
    - if no match is found, then return -1  
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0 
        high = len(nums) - 1 
        
        while low <= high: 
            middle = low + (high - low)//2 

            if nums[middle] == target: 
                return middle 
            elif nums[middle] < target: 
                low = middle + 1 
            else: 
                high = middle - 1

        return -1

        
        