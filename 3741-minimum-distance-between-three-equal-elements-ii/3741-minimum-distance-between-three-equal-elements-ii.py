class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos_map = defaultdict(list)
        min_dist = float('inf')
        found = False

        for curr_idx, val in enumerate(nums):
            indices = pos_map[val]

            if len(indices) == 2:
                dist = 2 * (curr_idx - indices[0])
                if dist < min_dist:
                    min_dist = dist
                found = True

                indices.pop(0)
                indices.append(curr_idx)

            else:
                indices.append(curr_idx)

        return min_dist if found else -1