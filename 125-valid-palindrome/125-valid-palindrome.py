class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            
            while not s[r].lower().isalnum() and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True
        
        ##OTHER SOLUTION
        #s = s.lower()
        #s = ''.join(c for c in s if c.isalnum())
        #return s == s[::-1]