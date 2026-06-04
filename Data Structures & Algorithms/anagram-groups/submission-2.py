'''
way to check for anagram: 
- if the length of strings is different -> not in anagram 
- store the frequencies of each character for first string 
- while iterating through the second string, subtract the frequency 
    - if frequency is < 0 for all characters, then anagram 

main issue here: 
    - how do you get two terms that might be anagrams together 

checking the anagram is easy -> we are just counting frequencies 

hashmap approach: 
    - if the word is an anagram -> each sorted word will be the same 
    - use this as a key in the hashmap 
    - init the hashmap as default dict, where the the value is a list 
    - O(m * n log n ), m = number of strings, n = longest string 

Improved Approach: 
    - init the key to be a frequency counter 
    - for each string in the input: 
        - init a frequncy array of size 26 with all 0s 
        - for char in string, increment counter 
        - use the frequncy array as key (convert to tuple)
        - append all of the words that match the frequency counter as 
        values 
    return set of values 


'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for s in strs: 
            count = [0] * 26 
            for c in s: 
                count[ord(c) - ord('a')] += 1
            
            result[tuple(count)].append(s)

        return list(result.values())

        
        
        