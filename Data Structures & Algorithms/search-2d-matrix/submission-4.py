"""
log (m * n) = binary search of n element m times 

-- high level algorithm: 

1. define a binary search helper method 
    - init a low, high pointer
        - low = first element 
        - high = last element 
    - start iterating: 
        - calculate the middle index 
        - if there is a match then return true 
        - if the middle value is higher, value on the left: 
            - set high to middle index 
        - if the middle value is lower, target on the right: 
            - set low to middle + 1 
    - return False otherwise 
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix: 
            if self.binary_search(row, target): 
                return True
        
        return False

    
    def binary_search(self, nums: List[int], target: int) -> bool: 
        """
        classic binary search to find an element 
        """

        low = 0 
        high = len(nums) - 1 

        while low <= high: 
            middle = low + (high - low) // 2 

            if nums[middle] == target: 
                return True 
            elif nums[middle] > target: 
                high = middle - 1 
            elif nums[middle] < target: 
                low = middle + 1 

        return False 






        