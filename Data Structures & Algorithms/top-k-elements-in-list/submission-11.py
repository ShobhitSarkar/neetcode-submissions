"""
two parts to the problem: 
    - counting frequencies 
        - init a map 
        - loop through the variables in nums 
        - if it exists in the map: 
            - increase counted frequency by one 
        - if it doesn't exist in the map:  
            - instantiate the frequency with 1 
    - sorting the frequencies to return results
        - we basically need to sort using the frequencies 
        - q: how do we get the number corresponding to the frequencies 
            - build an array containing the tuples (frequency, number)
            - sort the array (it gets sorted according to frequency)
            - get the first k values and then return the numbers a
                associated with the frequency 
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

        for freq in frequencies: 
            freq_array.append((frequencies[freq], freq))

        freq_array.sort(reverse = True) 

        result = [] 

        for i in range(k): 
            result.append(freq_array[i][1])    

        return result 











        