class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        index_map = defaultdict(list)
        for i, val in enumerate(nums):
            index_map[val].append(i)

        min_dist = float('inf')
        found = False

        for val in index_map:
            indices = index_map[val]
            if len(indices) >= 3:
                found = True

                for i in range(len(indices) -2):
                    current_dist = 2 * (indices[i+2] - indices[i])
                    min_dist = min(min_dist, current_dist)  
        return min_dist if found else -1