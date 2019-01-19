class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        num_rows = len(grid)
        if num_rows==0:
            return 0
        num_cols = len(grid[0])
        mask = [[1-int(grid[i][j]) for j in range(num_cols)] for i in range(num_rows)]
        count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if mask[i][j]:
                    continue
                count += 1
                node = (i,j)
                self.expand(node,grid,mask,num_rows,num_cols)
        return count
    
    def expand(self, node, grid, mask, num_rows, num_cols):
        lst = [node]
        dxdy = [(1,0), (-1,0), (0,1), (0,-1)]
        while len(lst)>0:
            node = lst.pop(0)
            for dx,dy in dxdy:
                ngh = (node[0]+dx, node[1]+dy)
                if self.inside(ngh, num_rows, num_cols) and mask[ngh[0]][ngh[1]]==0:
                    mask[ngh[0]][ngh[1]]=1
                    lst.append(ngh)
                
    def inside(self, node, num_rows, num_cols):
        return 0<=node[0]<num_rows and 0<=node[1]<num_cols