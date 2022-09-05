class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0#these will be start and end indices for the longest palindrome
        
        for i in range(len(s) - 1): #loop from 0 to len(s)-2
            length = max(self.expandAroundCenter(s, i, i),
                         self.expandAroundCenter(s, i, i + 1)) #deals with aba and aa as palindrome i.e length is even or odd
            if length > end - start: #if the newest length is bigger than the previous max
                start = i - (length - 1) // 2 #half of the string is behind i and half is past i, therefore i-length and i+length divided in 2 gives the start and end indices
                end = i + length // 2
            
        return s[start : end + 1]#return the new string 
    
    def expandAroundCenter(self, s: str, left: int, right: int):#same logic as leetcode 647
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return right - left - 1
