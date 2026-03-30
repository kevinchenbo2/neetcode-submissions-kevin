class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        optimal = [float('inf')] * len(cost)
        optimal[0] = cost[0]
        optimal[1] = cost[1]
        for i in range(2, len(cost)):
            optimal[i] = min(optimal[i - 1] + cost[i], optimal[i - 2] + cost[i])
        return min(optimal[len(cost) - 1], optimal[len(cost) - 2])