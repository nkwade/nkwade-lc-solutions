class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min, curr_max, res = 1, 1, nums[0]
        #the minimum may be multiplied by another negative number, making it larger than the maximum so that has to be kept track of
        #the current max of course has to be kept track of, that is trivial
        for num in nums: # loop through the entire array
            tmp = curr_min # curr_min will be multiplied or equal to the current number, which if it was used in curr_max calculation would use the same number twice, therefore the previous min has to be stored in a variable
            curr_min = min(curr_min * num, curr_max * num, num) #if the number is positive curr_min * num will produce a new min, if the number is negative then curr_max * num may produce a lower minimum, or if the curr_min is positive and the number is negative just the num will produce a lower minimum
            curr_max = max(curr_max * num, tmp * num, num)#same logic for min but reversed
            res = max(res, curr_max)#if the new max is larger then update the result
        return res#return the result which is garunteed to be the largest product subarray
    