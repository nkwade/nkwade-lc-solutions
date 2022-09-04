class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] #array of values that sum to the target value
        
        def dfs(i, curr, total): #dfs function that keeps track of 3 things
            #i = index in candidates that we are at
            #curr = list of the summed values that are not greater than the target
            #total = total sum of the values in the current array
            if total == target: #base case 1: the total sum of curr is equal to target
                res.append(curr.copy()) 
                #want to add a copy of the current array (we dont want to add its memory pointer) because it sums to the target value
                return
            if i >= len(candidates) or total > target: 
                #no more values in candidates to consider or if the total has exceeded the target with the last candidate addition
                return
            
            #now have 2 scenarios: continue searching the tree allowing reuse of the current candidate and searching the tree without reuse
            
            curr.append(candidates[i]) #this is the decision that allows reuse of the variable 
            dfs(i, curr, total + candidates[i]) #i doesnt shift due to reuse, total has now increased by candidates[i]
            curr.pop() #now we remove candidates[i] because this decision wont allow reuse of the value
            dfs(i+1, curr, total) #total and curr didnt change, i has shifted up 1
        
        dfs(0, [], 0) #start with i=0, curr is empty, sum is 0
        return res