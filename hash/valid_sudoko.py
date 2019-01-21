class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check all rows
        for row in board:
            if not self.valid_arr(row):
                return False
        # check all cols
        cols = [[row[i] for row in board] for i in range(9)]
        for col in cols:
            if not self.valid_arr(col):
                return False
        # check all boxes
        idxs = [[0,1,2],[3,4,5],[6,7,8]]
        for ti in idxs:
            for tj in idxs:
                box = [board[i][j] for i in ti for j in tj]
                if not self.valid_arr(box):
                    return False
        return True
        
    def valid_arr(self, row):
        count = [0]*9
        for ch in row:
            if ch=='.':
                continue
            elif count[int(ch)-1]:
                return False
            else:
                count[int(ch)-1]+=1
        return True


        [[7,6],[8,None,6],[5,8],[9],[1,None,3],[8,1],[6,8],[8,6],[2,None,4],[3,None,7],[9,0],[6,None,8],[1],[0,None,4],[4,7],[0,None,5],[3],[9,None,2],[4,None,0],[5],[2,4],[5,6],[7],[6,None,6],[0,5],[0,2],[6,None,5],[1,7],[3,8],[0,None,1],[2,None,8],[8],[1,4],[5,None,3],[6,None,0],[3,3],[1,0],[4,None,6],[1,None,5],[0],[1,2],[4,1],[9,None,9],[3,6],[2],[4,6],[0,8],[9,2],[4],[],[6],[2,None,1],[1,None,1],[1,1]]