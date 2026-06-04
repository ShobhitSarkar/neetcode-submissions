"""
- need to count frequency and store them - hashmap 
- iterate through the array while keeping track of the frequencies 
    - get all the frequencies, sort them 
    - return the top k elements 
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequencies = {}

        for num in nums: 
            if num in frequencies: 
                frequencies[num] += 1 
            else: 
                frequencies[num] = 1 

        freq_array = [] 
        
        for num in frequencies: 
            freq_array.append((frequencies[num], num))

        freq_array.sort(reverse=True)

        
        return [pair[1] for pair in freq_array[:k]]