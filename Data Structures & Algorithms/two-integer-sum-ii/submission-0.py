'''
- init left pointer and right pointer 

- move the two pointers towards each other: 
    - if the sum is equal -> then return indexes 
    - if sum is less, move left forward 
    - if sum is more, move right backward 

- when returning the indexes, add one to the indices 

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0 
        right = len(numbers) - 1

        while left < right: 
            if numbers[left] + numbers[right] == target: 
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target: 
                left += 1
            else: 
                right -= 1

    
        