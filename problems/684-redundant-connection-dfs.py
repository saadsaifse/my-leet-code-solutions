import re
from threading import currentThread
from typing import List, Set
'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacencyList = {}
        for i in range(1, len(edges) + 1):
            adjacencyList[i] = []

        # target of this function is to check if a connection exist from src to target
        # by looking at the neighbors of src. Add the nodes to visited list as you go through them
        # return true if src reaches target, else return false
        def dfs(src, target, visited):
            if src == target:
                return True
            if src not in visited:
                visited.add(src)
                neighbors = adjacencyList[src]
                for n in neighbors:
                    path = dfs(n, target, visited)
                    if path:
                        return True
            else:
                return False


        for a,b in edges:
            visited = set()

            if dfs(a, b, visited):
                return [a,b]

            adjacencyList[a].append(b)
            adjacencyList[b].append(a)
        return adjacencyList
       
                

if __name__ == "__main__":
    sol = Solution()
    print(sol.findRedundantConnection([[1,2], [1,3], [2,3]]))
    print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))