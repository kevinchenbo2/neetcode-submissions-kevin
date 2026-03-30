class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        neighbors = defaultdict(list)
        for c, p in prerequisites:
            neighbors[c].append(p)
        
        seen = set()
        scheduled = set()
        schedule = []

        def dfs(node):
            if node in seen:
                return False
            if neighbors[node] == []:
                if node not in scheduled:
                    schedule.append(node)
                    scheduled.add(node)
                return True
            seen.add(node)
            for n in neighbors[node]:
                if not dfs(n): return False
            seen.remove(node)
            neighbors[node] = []
            schedule.append(node)
            scheduled.add(node)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return schedule