class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
    
    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        if board[i][j] != word[0]:
            return False
        if board[i][j] == '!':
            return False   
        else: 
            board[i][j] = '!'
            if self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:]):
                return True
            else:
                board[i][j] = word[0]
                return False
