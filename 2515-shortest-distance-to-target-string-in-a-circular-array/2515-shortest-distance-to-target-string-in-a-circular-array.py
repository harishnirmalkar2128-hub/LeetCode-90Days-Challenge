class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        res = n
        found = False
        
        for i in range(n):
            if words[i] == target:
                found = True
                dist = abs(i - startIndex)
                res = min(res, dist, n - dist)
                
        if not found:
            return -1
            
        return res