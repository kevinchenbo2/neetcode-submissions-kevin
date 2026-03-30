class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]: 
        self.graph = defaultdict(dict)    
        for i in range(len(equations)):
            u, v = equations[i][0], equations[i][1]
            self.graph[u][v] = values[i]
            self.graph[v][u] = 1/values[i]
        
        ans = []
        for q in queries:
            start, end = q[0], q[1]
            ans.append(self.bfs(start, end))
        
        return ans
    
    def bfs(self, start, target):
        queue = deque([(start, 1)])
        visited = set()
        while queue:
            node, val = queue.popleft()
            for neighbor, weight in self.graph[node].items():
                if neighbor == target:
                    return weight * val
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, val * weight))
            
        
        return -1