'''

calculating the area: 
    - min between the two numbers * width difference (difference between pointer)

moving the pointers themselves: 
    - keep moving them towards each other while keeping track of the square 
    - if the distance between both of them keeps going down: 
        - it has to be matched by the column height
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0 
        right = len(heights) - 1

        max_area = min(heights[left], heights[right]) * (right - left)

        while left < right: 
            area = min(heights[left], heights[right]) * (right - left)
            if area > max_area: 
                max_area = area 
            
            if heights[left] < heights[right]: 
                left += 1
            else: 
                right -= 1

        
        return max_area
                



        