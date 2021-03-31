# 存储单词，需要标志位
class Trie:
    # 内部节点类
    class TrieNode:
        def __init__(self):
            self.children = [None] * 26
            self.isWord = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie.TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            cIdx = ord(c) - ord('a')
            if not node.children[cIdx]:
                node.children[cIdx] = Trie.TrieNode()
            node = node.children[cIdx]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            cIdx = ord(c) - ord('a')
            if not node.children[cIdx]:
                return False
            node = node.children[cIdx]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            cIdx = ord(c) - ord('a')
            if not node.children[cIdx]:
                return False
            node = node.children[cIdx]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
assert trie.search("apple")
assert not trie.search("app")
assert trie.startsWith("app")
trie.insert("app")
assert trie.search("app")
