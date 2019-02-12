import ipdb

# Definition for a Node.
class Node(object):
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root is None:
            return ''
        # leaf node
        elif len(root.children)==0:
            return str(root.val)
        ser = '(' + str(root.val) + ',' + self.serialize(root.children[0]) 
        for child in root.children[1:]:
            ser += ',' + self.serialize(child)
        ser += ')'        
        return ser
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if len(data)==0:
            return None
        return self.deser(data)[0]
        
    def deser(self, data):
        if len(data)==0:
            return []
        # has children
        if data[0]=='(' and data[-1]==')':
            idx = data.index(',')
            root = Node(int(data[1:idx]), self.deser(data[idx+1:-1]))
            return [root]    
        else:
            i = 0
            j = 0
            count = 0
            children = []
            while j<len(data):
                if data[j]==',' and count==0:
                    children+= self.deser(data[i:j])
                    i = j+1
                    count = 0
                elif data[j]=='(':
                    count += 1
                elif data[j]==')':
                    count -= 1
                j += 1
            if data[i]!='(':
                children += [Node(int(data[i:j]), [])]
            else:
                children += self.deser(data[i:j])
            return children
            
            
# Your Codec object will be instantiated and called as such:
codec = Codec()
root = Node(1)
root.children = [Node(x) for x in [3,2,4]]
root.children[0].children = [Node(x) for x in [5,6]]
coding = codec.serialize(root)
print(coding)
deco = codec.deserialize(coding)
print(deco)
ipdb.set_trace()