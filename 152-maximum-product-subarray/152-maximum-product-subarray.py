class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min, curr_max, res = 1, 1, nums[0]
        
        for num in nums:
            tmp = curr_min
            curr_min = min(curr_min * num, curr_max * num, num)
            curr_max = max(curr_max * num, tmp * num, num)
            res = max(res, curr_max)
        return res