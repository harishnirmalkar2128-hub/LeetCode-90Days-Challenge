class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Process each query
        for li, ri, ki, vi in queries:
            for idx in range(li, ri + 1, ki):
                nums[idx] = (nums[idx] * vi) % MOD
        
        # Step 2: Calculate bitwise XOR of all elements
        res = 0
        for x in nums:
            res ^= x
            
        return res