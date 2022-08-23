class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapCloseToOpen = {')': '(', '}':'{', ']':'['}
        
        for c in s:
            if c in mapCloseToOpen.values():
                stack.append(c)
            elif c in mapCloseToOpen.keys():
                if stack and mapCloseToOpen[c] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        return True if not stack else False