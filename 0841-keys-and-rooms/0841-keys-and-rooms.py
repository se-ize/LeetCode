from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        
        def bfs(v):
            queue = deque()
            queue.append(v)
            visited[v] = True
            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if visited[next_v] == False:
                        queue.append(next_v)
                        visited[next_v] = True
                    
        bfs(0)
    
        return all(visited)
        