class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.children = {}
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word = True

    def search(self, word: str) -> bool:
        # We use a recursive DFS to handle branching paths when we hit a '.'
        def dfs(index, root):
            current = root
            
            for i in range(index, len(word)):
                char = word[i]
                
                if char == '.':
                    # If it's a wildcard, we must check every child node
                    for child in current.children.values():
                        # If any of the branches return True, the word exists
                        if dfs(i + 1, child):
                            return True
                    # If we checked all children and none worked out, return False
                    return False
                else:
                    # Standard Trie traversal
                    if char not in current.children:
                        return False
                    current = current.children[char]
                    
            # Did we finish the word on a valid end node?
            return current.end_of_word
        
        # Start the DFS from index 0 and the root of the Trie
        return dfs(0, self.root)
            
        
