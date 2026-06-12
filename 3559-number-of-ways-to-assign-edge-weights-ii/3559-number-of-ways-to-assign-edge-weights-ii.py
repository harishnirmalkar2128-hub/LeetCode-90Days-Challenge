from typing import List
import sys

# Recursion limit badhana zaroori hai bade trees ke liye
sys.setrecursionlimit(200000)

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # 1. Total nodes nikalna (edges ki length + 1)
        n = len(edges) + 1
        
        # 2. Adjacency list banana
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 3. Binary lifting arrays setup karna
        LOG = 18  # Kyuki 2^17 > 10^5
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # 4. DFS function se depth aur parents find karna
        def dfs(node, parent, d):
            depth[node] = d
            up[node][0] = parent
            for child in adj[node]:
                if child != parent:
                    dfs(child, node, d + 1)
                    
        # Root node ko 1 maankar DFS chalana
        dfs(1, 1, 0)
        
        # 5. Binary lifting table fill karna
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        # 6. LCA (Lowest Common Ancestor) nikalne ka function
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
                
            # Dono ko same level/depth par lana
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            # Dono ko ek sath upar shift karna
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]
            
        # 7. Saari queries ko process karna
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
                continue
                
            # Dono nodes ke beech ka distance (L) nikalna
            lca = get_lca(u, v)
            L = depth[u] + depth[v] - 2 * depth[lca]
            
            # 2^(L-1) % MOD calculate karke append karna
            ways = pow(2, L - 1, MOD)
            answer.append(ways)
            
        return answer