class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        org_color = image[sr][sc]
        num_rows, num_cols = len(image), len(image[0])
        done = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        openlist = [(sr,sc)]
        while len(openlist)>0:
            cell = openlist.pop()
            image[cell[0]][cell[1]] = newColor
            if not done[cell[0]][cell[1]]:
                nghs = self.find_neighbors(cell, num_rows, num_cols)
                for ngh in nghs:
                    if image[ngh[0]][ngh[1]]==org_color and not done[ngh[0]][ngh[1]]:
                        openlist.append(ngh)
            done[cell[0]][cell[1]] = 1
        return image
                
    def find_neighbors(self, cell, num_rows, num_cols):
        dxdy = [(1,0), (-1,0), (0,1), (0,-1)]
        ans = []
        for dx,dy in dxdy:
            ngh = (cell[0]+dx, cell[1]+dy)
            if 0<=ngh[0]<num_rows and 0<=ngh[1]<num_cols:
                ans.append(ngh)
        return ans