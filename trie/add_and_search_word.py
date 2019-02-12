class Node:
    def __init__(self):
        self.children = [None]*26
        self.is_word = False


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()    

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            idx = ord(ch)-ord('a')
            # if child does not exist, create 
            if node.children[idx] is None:
                node.children[idx] = Node()
            node = node.children[idx]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.src(word, self.root)
    
    def src(self, word, node):
        for k,ch in enumerate(word):
            if ch=='.':
                for i in range(26):
                    rep = chr(ord('a') + i) + word[k+1:]
                    if self.src(rep, node):
                        return True
                return False
            else:
                idx = ord(ch) - ord('a')
                if node.children[idx] is None:
                    return False
                node = node.children[idx]
        return node.is_word


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)