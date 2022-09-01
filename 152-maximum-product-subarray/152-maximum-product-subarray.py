class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min, curr_max, ans = 1, 1, nums[0]
      
        for n in nums:
            tmp = curr_min
            curr_min = min(n * curr_min, n * curr_max, n)
            curr_max = max(n * curr_max, n * tmp, n)
            ans = max(ans, curr_max)
      
        return ans