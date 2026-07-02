"""
-- high level algorithm 

- init some variables: 
    - low = starting of the array 
    - high = pointer to last element of the array 
- move the pointers towards each other: 
    - find the middle pointer 
    - if the middle element is greater than target, element on the left
        - move the high element to middle - 1 
    - if middle element is lesser than target, element on the right: 
        - move the low element to middle + 1 
    - if exact match, return the middle index 
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0 
        high = len(nums) - 1 

        while low <= high: 
            middle = low + (high - low) // 2 

            if nums[middle] == target: 
                return middle 
            elif nums[middle] > target: 
                high = middle - 1
            elif nums[middle] < target: 
                low = middle + 1 

        return -1
