"""
-- given: 
    - matrix with arrays (sorted)
    - constraint: log(mn)

-- to find: 
    - target

-- high level algorithm: 
    - binary search for each individual array 
    - repeat that for each individual array in the matrix 

-- binary search algorithm: 
    - init low, high pointers 
    - start iterating through the array (while the pointers don't converge): 
        - calculate a middle index 
        - if nums[middle index] > target: 
            - targe is on the left side, high = middle - 1 
        - if nums[middle index] < target: 
            - target is on the right side, low = middle + 1 
        - if nums[middle index] is the target: 
            - return true 
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 

        for row in matrix: 
            if self.binary_search(row, target): 
                return True 

        return False 
    

    def binary_search(self, nums: List[int], target) -> bool: 
        """
        helper method to do binary search 
        """

        low = 0 
        high = len(nums) - 1 

        while low <= high: 
            mid = low + (high - low) // 2 

            if nums[mid] == target: 
                return True 
            elif nums[mid] > target: 
                high = mid - 1 
            else: 
                low = mid + 1

        return False 








        