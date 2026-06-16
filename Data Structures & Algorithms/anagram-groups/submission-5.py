"""
-- high level algo

anagram = same characters, same frequency 

- initialize a default dict 
- sorted version of the word acts as unique key 
- iterate through the given array of strings and then append 
    accordng to the key 
- building the result: 
    - create an array to store the results 
    - iterate through the default dict and append results to the array 
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        store = defaultdict(list)

        for string in strs: 
            key = self._sort_word(string)
            store[key].append(string)

        result = [] 

        for key in store:
            result.append(store[key])

        return result 

    def _sort_word(self, word: str) -> str: 
        """
        sorts a given word 
        """

        word_array = [] 
        for char in word: 
            word_array.append(char)
        
        word_array.sort()

        return "".join(word_array)
        