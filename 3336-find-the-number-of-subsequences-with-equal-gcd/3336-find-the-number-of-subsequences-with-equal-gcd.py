import math
from collections import defaultdict
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        # dp dictionary maps (gcd1, gcd2) -> total ways
        # 0 means the subsequence is empty
        dp = defaultdict(int)
        dp[(0, 0)] = 1
        
        for x in nums:
            next_dp = defaultdict(int)
            
            for (g1, g2), count in dp.items():
                count %= MOD
                
                # Choice 1: Do not include x in either sequence
                next_dp[(g1, g2)] = (next_dp[(g1, g2)] + count) % MOD
                
                # Choice 2: Include x in seq1
                new_g1 = math.gcd(g1, x)
                next_dp[(new_g1, g2)] = (next_dp[(new_g1, g2)] + count) % MOD
                
                # Choice 3: Include x in seq2
                new_g2 = math.gcd(g2, x)
                next_dp[(g1, new_g2)] = (next_dp[(g1, new_g2)] + count) % MOD
                
            dp = next_dp
            
        ans = 0
        # Sum up all ways where both GCDs are equal and not 0
        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 > 0:
                ans = (ans + count) % MOD
                
        return ans