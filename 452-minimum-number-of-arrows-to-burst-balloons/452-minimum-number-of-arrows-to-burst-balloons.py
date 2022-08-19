# core idea: need to find largest point --> inlcude more positions

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        position = points[0][1]
        count = 1
        
        for i in range(len(points)):
            if points[i][0] <= position:
                continue
            else:
                position = points[i][1]
                count = count + 1
        return count