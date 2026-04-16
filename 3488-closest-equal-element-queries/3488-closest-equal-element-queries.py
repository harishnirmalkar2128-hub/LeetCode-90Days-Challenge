class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos_map = {}
        for idx, val in enumerate(nums):
            if val not in pos_map:
                pos_map[val] = []
            pos_map[val].append(idx)

        results = []
        for q_idx in queries:
            val = nums[q_idx]
            indices = pos_map[val]

            if len(indices) <= 1:
                results.append(-1)
                continue
            
            curr_pos = bisect_left(indices, q_idx)
            min_dist = n
            
            neighbors = []
            if curr_pos > 0:
                neighbors.append(indices[curr_pos - 1])
            if curr_pos < len(indices) - 1:
                neighbors.append(indices[curr_pos + 1])
            
            neighbors.append(indices[0])
            neighbors.append(indices[-1])
            
            for neighbor in neighbors:
                if neighbor == q_idx:
                    continue
                d = abs(neighbor - q_idx)
                min_dist = min(min_dist, d, n - d)
                
            results.append(min_dist)
            
        return results