class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0 #this is the count of palindroms
        
        for i in range(len(s)): #for each character in the string
            left, right = i, i #set left and right pointers as the character index
            while left >= 0 and right < len(s) and s[left] == s[right]:#while the characters are the same around the center character i.e palindrome
                left -= 1
                right += 1
                res += 1
            
            l, r = i, i+1 #this is because you could have a palindrome be aba or aa, the loop deals with aba this loop deals with aa
            
            while 0 <= l and r < len(s) and s[l] == s[r]: #same logic as before
                res += 1
                r += 1
                l -= 1
        return res #return the number of palindroms