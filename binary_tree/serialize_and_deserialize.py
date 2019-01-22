# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        sz = self.level_ser(root)
        print(sz)
        return str(sz)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        sz = data.replace(" ","")[1:-1]
        ser = sz.split(",")
        return self.level_deser(ser)
        
    def level_ser(self, root):
        if root is None:
            return []
        
        # serialize level by level
        openlist = [root]
        sz = [root.val]
        while len(openlist)>0:
            n = len(openlist)
            for _ in range(n):
                node = openlist.pop(0)
                if node.left is not None:
                    openlist.append(node.left)
                    sz.append(node.left.val)
                else:
                    sz.append(None)
                if node.right is not None:
                    openlist.append(node.right)
                    sz.append(node.right.val)
                else:
                    sz.append(None)
        # remove any trailing Nones
        i = len(sz)-1
        while i>0:
            if sz[i] is None:
                i-=1
            else:
                break
        return sz[:i+1]
    
    def level_deser(self, ser):
        # empty tree
        if len(ser)==1 and ser[0]=='':
            return None
        
        root = TreeNode(int(ser[0]))
        openlist = [root]
        i = 1
        while i<len(ser):
            node = openlist.pop(0)
            # left child
            if ser[i]=='None':
                node.left = None
            else:
                new_node = TreeNode(int(ser[i]))
                node.left = new_node
                openlist.append(new_node)
            i += 1
            if i==len(ser):
                break
            # right child
            if ser[i]=='None':
                node.right = None
            else:
                new_node = TreeNode(int(ser[i]))
                node.right = new_node
                openlist.append(new_node)
            i += 1
            
        return root
    
    def ser(self, node):
        # bottom up approach
        # inefficient for highly skewed trees
        if node is not None:
            left_ser = self.ser(node.left)
            right_ser = self.ser(node.right)
            # leaf node
            if left_ser == [None] and right_ser == [None]:
                node_ser = [node.val]
            else:
                diff = len(left_ser) - len(right_ser)
                if diff > 0:
                    pad_size = (len(left_ser)+1)//(len(right_ser)+1)-1
                    padding = [None]*pad_size
                    right_ser = self.pad_nones(right_ser, padding)
                elif diff < 0:
                    pad_size = (len(right_ser)+1)//(len(left_ser)+1)-1
                    padding = [None]*pad_size
                    left_ser = self.pad_nones(left_ser, padding)
                node_ser = left_ser + [node.val] + right_ser
            return node_ser
        return [None]
    
    def pad_nones(self, ser, padding):
        # utility for making left and right subtrees equal in depth
        new_ser = []
        for i in range(len(ser)):
            if i%2==0:
                new_ser += padding + [ser[i]] + padding
            else:
                new_ser += [ser[i]]
        return new_ser
    
    def deser(self, ser):
        # deserialization for ser method 
        mid = len(ser)//2
        if len(ser)==0 or ser[mid]=='None':
            return None
        node = TreeNode(int(ser[mid]))
        node.left = self.deser(ser[:mid])
        node.right = self.deser(ser[mid+1:])
        return node
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))