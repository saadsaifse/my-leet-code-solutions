from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def dfs(u,v):
            if u in visited:
                return False
            if u == v:
                return True
            
            visited.add(u)
            
            for i in graph[u]:
                if dfs(i, v):
                    return True
            return False
        
        
        n = len(edges)
        graph = defaultdict(list)
        
        
        ans = []
        for u, v in edges:
            visited = set()
            if dfs(u, v):
                ans = [u,v]
            graph[u].append(v)
            graph[v].append(u)
        return ans





# First solution where I ended up simply traversing the graph lol

# from typing import List
# from collections import deque

# class Graph:
#     def __init__(self, edges) -> None:        
#         self.edges = edges
#         self.adjList = [[] for _ in range(0, len(edges)+1)]
#         for (u, v) in edges:
#             self.adjList[u].append(v)
#             self.adjList[v].append(u)
#         del self.adjList[0]
#         self.vertices = len(self.adjList)


# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

#         def recursiveBFS(discovered, queue):
#             if not queue:
#                 return
#             v = queue.popleft()
#             print(v)
#             if v:
#                 neighbors = graph.adjList[v-1]
#                 for n in neighbors:
#                     if n not in discovered:
#                         discovered.add(n)                        
#                         queue.append(n)
#                 recursiveBFS(discovered, queue)

#         graph = Graph(edges)
#         print(graph.adjList)
#         queue = deque()
#         discovered = set()
#         # for v in range(1, graph.vertices+1):
#             # if v not in discovered:
#         v = 1
#         discovered.add(1)                
#         queue.append(v)
#         recursiveBFS(discovered, queue)
        
#         return []


if __name__ == "__main__":
    sol = Solution()
    #sol.findRedundantConnection([[1,2],[1,3],[2,3]])
    sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]])

