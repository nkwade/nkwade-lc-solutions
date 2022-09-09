class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 #initialize the left and right pointers

        while l <= r:#if r ever becomes greater than l then the value doesnt exist
            mid = (l + r) // 2 #get the middle of the array

            if nums[mid] == target:#if we found the target just return the index
                return mid

            if nums[l] <= nums[mid]: #if we are the bottom half of the values in the array
                if target > nums[mid] or target < nums[l]: #if the target is not in the range between the left and middle values
                    l = mid + 1#increase the left pointer to the mid plus one because we know the target is not in this range
                else:
                    r = mid - 1#decrease the right pointer to the mid minus one because we know the target is in this range
            else: #if we are in the upper half of the values in the array
                if target < nums[mid] or target > nums[r]:#the target is outside of the range between mid and r
                    r = mid - 1 #lower r to mid - 1
                else:
                    l = mid + 1#target is inside the range between mid and r therefore move l to mid + 1
        return -1