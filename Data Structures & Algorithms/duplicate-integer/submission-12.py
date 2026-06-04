"""
- init a hashmap to keep track of visited 
- start iterating in the array: 
    - if the number exists in the hashmap 
        return false 
    - if doesn't then add to hashmap 
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        visited={} 

        for num in nums: 
            if num in visited: 
                return True
            else: 
                visited[num] = False 

        return False
        