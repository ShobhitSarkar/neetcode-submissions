"""
approach 1: sorting

    - sort the entire array 
    - loop through the array and then return the kth element 
    - tradeoff: we don't need the entire array to be sorted, we only need top k 

approach 2: max heap 
    - convert all the number to negative 
    - heapify it 
    - move through the array 
        - pop the kth element & return it 
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [] 

        for num in nums: 
            heap.append(-num)

        heapq.heapify(heap)

        top_k = [] 

        for _ in range(k): 
            top_k.append(heapq.heappop(heap))
        
        return -top_k.pop()
        