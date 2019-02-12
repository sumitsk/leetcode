import ipdb

# Definition for a Node.
class Node(object):
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        return self.encode_recur(root, [])
        
    def encode_recur(self, node, siblings):
        root = TreeNode(node.val)
        children = node.children
        if len(children)>0:
            root.left = self.encode_recur(children[0], children[1:])
        if len(siblings)>0:
            root.right = self.encode_recur(siblings[0], siblings[1:])
        return root
            
    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        
        :type data: TreeNode
        :rtype: Node
        """
        if data is None:
            return None
        return self.decode_recur(data)[0]
    
    def decode_recur(self, node):
        if node is None:
            return []
        root = Node(node.val, self.decode_recur(node.left))
        return [root] + self.decode_recur(node.right)

if __name__ == '__main__':
    root = Node(1)
    root.children = [Node(x) for x in range(2,6)]
    root.children[0].children = [Node(x) for x in [6,7]]
    root.children[1].children = [Node(x) for x in [8,13]]
    root.children[1].children[0].children = [Node(x) for x in [9,12]]
    root.children[1].children[0].children[0].children = [Node(x) for x in [10,11]]
    root.children[2].children = [Node(15)]
    root.children[3].children = [Node(16)]

    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    coding = codec.encode(root)
    decode = codec.decode(coding)
    ipdb.set_trace()