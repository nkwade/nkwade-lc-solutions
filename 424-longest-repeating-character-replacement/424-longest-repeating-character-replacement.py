class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = defaultdict(int) #Initialize count with defaultdict to increment count for new letters
        
        maxFreq = 0 #keep track of a count for a letter with maximum occurence rate
        l = 0 #left pointer of a window
        for r in range(len(s)): #r indicates right pointer of the window
            count[s[r]] += 1 #increase the character count for that characters
            maxFreq = max(maxFreq, count[s[r]]) #keep track of the characters with the highest frequency
            
            if (r - l + 1) - maxFreq > k: #if the size of the window minus the most occuring character in that window is greater than the replacement, then remove the character to the left of the windows count by 1 and then increase the left pointer by 1
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1) #get the longest repeating character substring with replacement
        return res