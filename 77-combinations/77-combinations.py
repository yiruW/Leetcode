class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        
        def backTracking(n, k, startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(startIndex, n + 1):
                path.append(i)
                backTracking(n, k, i+1)
                path.pop()
                
        backTracking(n, k, 1)
        return res