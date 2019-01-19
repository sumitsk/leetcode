# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        root = UndirectedGraphNode(node.label)
        openlist = [(node, root)]
        while len(openlist)>0:
            node, copy_node = openlist.pop(0)
            if not hasattr(node, 'visited'):
                for ngh in node.neighbors:
                    copy_ngh = UndirectedGraphNode(ngh.label)
                    copy_node.neighbors.append(copy_ngh)
                    openlist.append((ngh, copy_ngh))
                node.visited = True
        
        return root