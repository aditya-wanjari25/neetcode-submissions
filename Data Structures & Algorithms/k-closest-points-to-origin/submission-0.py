import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            min_heap.append((distance,point))
            
        heapq.heapify(min_heap)

        result = []
        while k > 0:
            dist , point = heapq.heappop(min_heap)
            result.append(point)
            k-=1
        
        return result


        

        