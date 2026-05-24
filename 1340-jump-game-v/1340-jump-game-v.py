class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n
        
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            
            max_visited = 1
            
            # Check Right Jumps
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                max_visited = max(max_visited, 1 + dfs(j))
                
            # Check Left Jumps
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= arr[i]:
                    break
                max_visited = max(max_visited, 1 + dfs(j))
                
            dp[i] = max_visited
            return dp[i]
            
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
            
        return ans