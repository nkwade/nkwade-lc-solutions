class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                return cur
            nums[cur] = -nums[cur]
        
        nums.sort()#trivial
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]