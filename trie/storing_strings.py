class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def char_to_index(self, char):
        return ord(char)-ord('a')

    def insert(self, key):
        tail = self.root
        length = len(key)
        for char_index in range(length):
            index = self.char_to_index(key[char_index])

            if tail.children[index] is None:
                tail.children[index] = TrieNode()
            tail = tail.children[index]

        tail.isEndOfWord = True

    def create_set(self, arr):
        for a in arr:
            self.insert(a)

    def search(self, key):
        tail = self.root
        length = len(key)
        for char_index in range(length):
            index = self.char_to_index(key[char_index])

            if tail.children[index] is None:
                return False
            tail = tail.children[index]

        return tail is not None and tail.isEndOfWord == True


if __name__ == '__main__':
    keys = ['kasztan', 'janusz', 'tracz', 'osa', 'zbigngiew', 'kremowka']

    trie = Trie()
    trie.create_set(keys)

    print(trie.search('osa'))