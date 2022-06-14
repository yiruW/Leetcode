class Solution:
    def dfs(self, key:int, rooms:List[List[int]], visited:List[bool]):
        if visited[key]:
            return
        visited[key] = True
        key = rooms[key]
        for i in range(len(key)):
            self.dfs(key[i], rooms, visited)
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for i in range(len(rooms))]
        self.dfs(0, rooms, visited)
        
        for i in range(len(visited)):
            if not visited[i]:
                return False 
        return True