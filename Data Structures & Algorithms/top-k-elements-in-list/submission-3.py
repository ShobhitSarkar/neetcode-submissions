'''
- process nums in the array
- hashmap = 
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {} 

        for num in nums: 
            if num in freq: 
                freq[num] += 1 
            else: 
                freq[num] = 1 
        
        frequencies = [] 

        for num in freq: 
            frequencies.append(freq[num])

        frequencies.sort(reverse = True)
        value = frequencies[k-1]

        result = [] 

        for element in freq: 
            if freq[element] >= value: 
                result.append(element)

        return result

        