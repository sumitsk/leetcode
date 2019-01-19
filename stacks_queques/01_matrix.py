class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        num_rows, num_cols = len(matrix), len(matrix[0])
        dist = [[None for _ in range(num_cols)] for _ in range(num_rows)]
        openlist = []
        # find all cells with 0
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j]==0:
                    openlist.append((i,j))
        
        val = 0
        # expand from all 0 cells
        while len(openlist)>0:
            n = len(openlist)
            for _ in range(n):
                cell = openlist.pop(0)
                # visited for the first time
                if dist[cell[0]][cell[1]] is None:
                    dist[cell[0]][cell[1]] = val
                    nghs = self.find_neighbors(cell, num_rows, num_cols)
                    for ngh in nghs:
                        # do not add to list if dist is more or equal to val
                        if dist[ngh[0]][ngh[1]] is None:
                            openlist.append(ngh)
            val += 1
        return dist
    
        
    def find_neighbors(self, cell, num_rows, num_cols):
        dxdy = [(1,0), (-1,0), (0,1), (0,-1)]
        ans = []
        for dx,dy in dxdy:
            ngh = (cell[0]+dx, cell[1]+dy)
            if 0<=ngh[0]<num_rows and 0<=ngh[1]<num_cols:
                ans.append(ngh)
        return ans