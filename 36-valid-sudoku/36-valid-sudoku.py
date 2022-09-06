class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def init_mapper():
            return {i: {} for i in range(9)}
        
        mapper_row = init_mapper()
        mapper_col = init_mapper()
        mapper_box = init_mapper()
        pos_box = {
            (0,0): 0,
            (0,1): 1,
            (0,2): 2,
            (1,0): 3,
            (1,1): 4,
            (1,2): 5,
            (2,0): 6,
            (2,1): 7,
            (2,2): 8,
        }
        
        for r, row in enumerate(board):
            for c, item in enumerate(row):
                if item == ".":
                    continue
                b = pos_box[(r // 3, c // 3)]
                if mapper_row[r].get(item, False) or mapper_col[c].get(item, False) or mapper_box[b].get(item, False):
                    # repeated item
                    return False
                else:
                    mapper_row[r][item] = True
                    mapper_col[c][item] = True
                    mapper_box[b][item] = True
                
        return True