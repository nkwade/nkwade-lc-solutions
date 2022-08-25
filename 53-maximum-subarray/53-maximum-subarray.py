class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp, out = [], nums[0]
        dp.append(nums[0])
        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))
            out = max(out, dp[i])
        
        return out