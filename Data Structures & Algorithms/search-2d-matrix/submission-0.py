"""
-- high level algorithm: 
    - we're basically searching for a number in multiple arrays 

x - binary search algo: 
    - init couple of pointers: 
        - low = 0 
        - high = len(nums) - 1 
    - while the low is not equal to the high: 
        - calculate the middle index 
        - if the nums of the middle index is target: 
            - then return true 
        - if nums[middle] is lower than target, number is on the right 
            - low = middle + 1 
        - else number is on the left side of middle 
            - high = middle - 1 

x - consuming the binary search method: 
    - iterate through the arrays given in the matrix array 
    - return true if we get a hit from binary search 
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix: 
            if self.binary_search(row, target): 
                return True

        return False

    

    def binary_search(self, nums: List[int], target) -> bool: 
        """
        - helper method to do binary search for a given array 
        - returns true if target in array, false otherwise 
        """

        low = 0 
        high = len(nums) - 1 

        while low <= high: 
            middle = low + (high - low) // 2 
            
            if nums[middle] == target: 
                return True 
            elif nums[middle] < target: 
                low = middle + 1 
            else: 
                high = middle - 1 

        return False 
        