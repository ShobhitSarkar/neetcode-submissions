"""
-- high level algorithm: 

    - create another array with negative stones values 
    - heapify it (it will give us a max heap)
    - pop the first two elements 
        - if they're not equal, then push the remainder on it 
    - keep doing this untill there is 1 or 0 element, return condition as necessary 
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [] 

        for stone in stones: 
            heap.append(-stone)

        heapq.heapify(heap)

        while len(heap) > 1: 
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first != second: 
                heapq.heappush(heap, -abs(second-first))
        
        return -heap[0] if len(heap) == 1 else 0
        