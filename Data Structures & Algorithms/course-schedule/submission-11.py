class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = defaultdict(list)
        for p in prerequisites:
            neighbors[p[0]].append(p[1])
        
        if len(prerequisites) < 1:
            return True
        
        seen = set()
        
        def dfs(node):
            if node in seen:
                return False
            if neighbors[node] == []:
                return True
            seen.add(node)
            for n in neighbors[node]:
                if not dfs(n): return False
            seen.remove(node)
            neighbors[node] = []
            return True
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True