class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [0]*len(rooms)
        visited[0] = 1
        openlist = rooms[0]
        while len(openlist)>0:
            r = openlist.pop()
            visited[r] = 1
            next_rooms = rooms[r]
            for room in next_rooms:
                if visited[room]==0:
                    openlist.append(room)
                    
        if sum(visited)==len(rooms):
            return True
        return False