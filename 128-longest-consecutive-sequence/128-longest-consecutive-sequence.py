class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    num_set = set(nums)
    long = 0
    
    for num in num_set:
      if num-1 not in num_set:
        curr_num = num
        curr = 1
        
        while curr_num + 1 in num_set:
          curr_num += 1
          curr += 1
        
        long = max(long, curr)
    
    return long