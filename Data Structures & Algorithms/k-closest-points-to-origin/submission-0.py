"""
-- high level algorithm: 

    - init an array 
        - this is later going to become our heap
    - for each of the point: 
        - create a tuple: (-distance, [point])
        - append it to the heap array 
    - heapify the array 
    - init a top_k and then pop the elements our the array 
    - return the final array with the points in top_k array 
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = [] 

        for point in points: 
            distance = point[0] ** 2 + point[1] ** 2 
            heap.append((distance, point))

        heapq.heapify(heap)

        top_k = [] 

        for _ in range(k): 
            top_k.append(heapq.heappop(heap))

        return [point for distance, point in top_k]
        