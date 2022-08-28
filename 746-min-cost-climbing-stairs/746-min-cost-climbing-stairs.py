class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = []
        dp.append(cost[0])
        dp.append(cost[1])
        
        for i in range(2, len(cost)):
            dp.append(min(cost[i] + dp[i-1], cost[i] + dp[i-2]))
        
        return min(dp[len(cost) - 1], dp[len(cost) - 2])