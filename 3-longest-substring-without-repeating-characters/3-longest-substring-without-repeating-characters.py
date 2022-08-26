class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, res = 0, 0
        
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        
        return res