"""
-- high level algorithm: 

x- counting frequency 
    - init a hashmap to count the frequencies of each of the numbers 
    - iterate through the nums array: 
        - if num is in hashmap, increment the count 
        - if the num is not in hashmap, add with frequency one 

x - sorting the frequency: 
    - instantiate an array 
    - build out an array with with the (frequency, num) tuples 
    - sort the array 
    - iterate k times: 
        - return the second value of these tuples into a result array and return 
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if not nums: 
            return [] 
        
        frequencies = {} 

        for num in nums: 
            if num in frequencies: 
                frequencies[num] += 1
            else: 
                frequencies[num] = 1 

        frequent = [] 

        for num in frequencies: 
            current = (frequencies[num], num)
            frequent.append(current)

        frequent.sort(reverse=True) 

        return [pair[1] for pair in frequent[:k]]

        