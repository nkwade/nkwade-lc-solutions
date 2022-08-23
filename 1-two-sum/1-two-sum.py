class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        
        for i in range(len(nums)):
            if target - nums[i] in hm.keys():
                return [i, hm[target-nums[i]]]
            hm[nums[i]] = i
        