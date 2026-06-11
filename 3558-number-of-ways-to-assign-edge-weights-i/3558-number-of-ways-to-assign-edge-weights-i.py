from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        n = len(edges) + 1
        
        # Step 1: Adjacency list banao tree ki
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Step 2: BFS use karke maximum depth dhoondho (Root = 1)
        max_depth = 0
        queue = deque([(1, 0)])  # (node, current_depth/edges_count)
        visited = [False] * (n + 1)
        visited[1] = True
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, depth + 1))
                    
        # Step 3: Agar max_depth L hai, toh answer 2^(L-1) % (10^9 + 7) hoga
        MOD = 10**9 + 7
        return pow(2, max_depth - 1, MOD)