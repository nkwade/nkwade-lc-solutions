class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        t = list(t)
        for c in s:
            if c not in t:
                return False
            t.remove(c)
        
        return True if not t else False