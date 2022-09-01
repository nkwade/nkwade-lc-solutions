class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        low, high = [1] * len(nums), [1] * len(nums)
        low[0] = nums[0]
        high[0] = nums[0]
        out = nums[0]
        
        for i in range(1, len(nums)):
            low[i] = min(high[i-1] * nums[i], low[i-1] * nums[i], nums[i])
            high[i] = max(high[i-1] * nums[i], low[i-1] * nums[i], nums[i])
            out = max(out, high[i])
        return out