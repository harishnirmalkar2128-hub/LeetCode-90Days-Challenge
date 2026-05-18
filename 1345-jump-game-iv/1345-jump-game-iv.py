class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
            
        graph = collections.defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        queue = collections.deque([(0, 0)])
        visited = {0}
        
        while queue:
            idx, steps = queue.popleft()
            
            if idx == n - 1:
                return steps
                
            neighbors = [idx - 1, idx + 1]
            if arr[idx] in graph:
                neighbors.extend(graph[arr[idx]])
                del graph[arr[idx]]
                
            for nxt in neighbors:
                if 0 <= nxt < n and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
                    
        return -1