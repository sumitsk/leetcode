class Node:
    def __init__(self):
        self.children = [None]*26
        self.is_word = False

class Trie(object):

    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            idx = ord(ch)-ord('a')
            # if child does not exist, create 
            if node.children[idx] is None:
                node.children[idx] = Node()
            node = node.children[idx]
        node.is_word = True
        
    def replacement(self, word):
        node = self.root
        for i, ch in enumerate(word):
            if node.is_word:
                return word[:i]
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                return word
            node = node.children[idx]
        return word
    
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        self.data = Trie()
        for word in dict:
            self.data.insert(word)
        ans = []
        lst = sentence.split(' ')
        for word in lst:
            ans.append(self.data.replacement(word))
        return ' '.join(ans)
            