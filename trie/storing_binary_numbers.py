class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        tail = self.root
        length = len(key)
        for index in range(length):
            bit = int(key[index])

            if not tail.children[bit]:
                tail.children[bit] = TrieNode()
            tail = tail.children[bit]

        tail.isEndOfWord = True

    def create_set(self, arr):
        for a in arr:
            self.insert(a)

    def search(self, key):
        tail = self.root
        length = len(key)
        for index in range(length):
            bit = int(key[index])

            if not tail.children[bit]:
                return False
            tail = tail.children[bit]

        return tail is not None and tail.isEndOfWord


if __name__ == '__main__':
    keys = ['10011', '1', '10', '101', '110111', '1101011']

    trie = Trie()
    trie.create_set(keys)

    print(trie.search('110111'))
