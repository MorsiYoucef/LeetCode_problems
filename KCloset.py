import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        for i in range(len(points)):
            distance = math.sqrt(pow(points[i][0],2) + pow(points[i][1],2)) 
            dis.append([distance,points[i][0],points[i][1]])
        heapq.heapify(dis)
        res = []
        for i in range(k):
            dist,x,y = heapq.heappop(dis)
            res.append([x,y])
        return res