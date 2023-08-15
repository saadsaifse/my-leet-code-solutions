class WeightedGraph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        
        self.g = defaultdict(list)
        for c in self.edges:
            self.g[c[0]].append((c[1], 0))
            self.g[c[1]].append((c[0], 1))
        print(self.g)


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = WeightedGraph(n, connections)        
        def toZero(node, g, visited) -> int:
            if node in visited:
                return 0            
            visited.add(node)
            startingNode = node
            count = 0
            for targetNode, direction in g[node]:
                if targetNode in visited:
                    continue
                if direction == 0:
                    count += 1
                c = toZero(targetNode, g, visited)                        
                count += c
            return count
            
        return toZero(0, graph.g, set())