class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1
        
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        global_best_idx = 0
        min_len = len(wordsContainer[0])
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < min_len:
                min_len = len(wordsContainer[i])
                global_best_idx = i
                
        root.best_idx = global_best_idx
        
        for i, word in enumerate(wordsContainer):
            curr = root
            w_len = len(word)
            
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                if curr.best_idx == -1:
                    curr.best_idx = i
                else:
                    curr_best_len = len(wordsContainer[curr.best_idx])
                    if w_len < curr_best_len:
                        curr.best_idx = i
                    elif w_len == curr_best_len:
                        if i < curr.best_idx:
                            curr.best_idx = i
                            
        ans = []
        for query in wordsQuery:
            curr = root
            matched_idx = root.best_idx
            
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                    matched_idx = curr.best_idx
                else:
                    break
            ans.append(matched_idx)
            
        return ans