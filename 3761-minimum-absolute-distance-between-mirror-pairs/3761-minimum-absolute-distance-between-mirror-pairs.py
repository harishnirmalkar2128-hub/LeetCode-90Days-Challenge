class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        def get_reverse(n):
            return int(str(n)[::-1])
        
        target_map = {}
        min_dist = float('inf')
        
        for j in range(len(nums)):
            current_val = nums[j]
            
            if current_val in target_map:
                current_dist = j - target_map[current_val]
                if current_dist < min_dist:
                    min_dist = current_dist
            
            rev = get_reverse(current_val)
            target_map[rev] = j
            
        if min_dist == float('inf'):
            return -1
            
        return min_dist