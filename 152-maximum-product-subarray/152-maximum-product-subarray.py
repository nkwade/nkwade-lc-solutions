class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min, curr_max, ans = 1, 1, nums[0]
      
        for n in nums:
            curr_min, curr_max = min(n * curr_min, n * curr_max, n),  max(n * curr_max, n * curr_min, n)
            ans = max(curr_max, ans)
        return ans