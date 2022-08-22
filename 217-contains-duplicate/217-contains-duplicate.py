class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = dict()
        
        for num in nums:
            if num in hm.keys():
                return True
            hm[num] = num
        
        return False