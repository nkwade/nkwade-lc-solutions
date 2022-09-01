class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        one, two = 0, 0

        for n in nums:
            tmp = max(n +  one, two)
            one = two
            two = tmp
    
        return two