class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
          dp[i] = dp[i-1] * nums[i-1]
        
        r_prod = 1
        for r in range(len(nums) - 1, -1, -1):
          dp[r] *= r_prod
          r_prod *= nums[r]
        
        return dp