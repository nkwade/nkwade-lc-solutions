class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def search(k, i, j):
            if k == len(word):
                return True
            if(i<0 or j<0 or i==len(board) or j==len(board[0]) or board[i][j]!=word[k]):
                return False
            ch=board[i][j]
            board[i][j]="#"
            opt1=search(k+1, i+1,j)
            opt2=search(k+1, i-1,j)
            opt3=search(k+1, i,j+1)
            opt4=search(k+1, i,j-1)
            board[i][j]=ch
            return(opt1 or opt2 or opt3 or opt4)
        
        n=len(board)
        m=len(board[0])

        for i in range(0,n):
            for j in range(0,m):
                if(board[i][j]==word[0]):
                    if(search(0,i,j)):
                        return True
        return False