class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_n = len(nums)
        l, r = 0, len_n - 1
        
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        
        return -1