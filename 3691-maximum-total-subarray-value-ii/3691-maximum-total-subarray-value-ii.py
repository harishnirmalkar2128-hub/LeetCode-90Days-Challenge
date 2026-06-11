import math
from heapq import heappush, heappop

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        logn = n.bit_length()
        
        # Sparse Table initialize karna
        stMax = [[0] * logn for _ in range(n)]
        stMin = [[0] * logn for _ in range(n)]
        
        for i in range(n):
            stMax[i][0] = stMin[i][0] = nums[i]
            
        for j in range(1, logn):
            for i in range(n - (1 << j) + 1):
                stMax[i][j] = max(stMax[i][j - 1], stMax[i + (1 << (j - 1))][j - 1])
                stMin[i][j] = min(stMin[i][j - 1], stMin[i + (1 << (j - 1))][j - 1])
                
        # Max Heap banana
        pq = []
        for l in range(n):
            j = (n - l).bit_length() - 1
            mx = max(stMax[l][j], stMax[n - (1 << j)][j])
            mn = min(stMin[l][j], stMin[n - (1 << j)][j])
            heappush(pq, (-(mx - mn), l, n - 1))
            
        ans = 0
        while k > 0 and pq:
            val, l, r = heappop(pq)
            ans += (-val)
            k -= 1
            
            if r > l:
                j = (r - 1 - l + 1).bit_length() - 1
                mx = max(stMax[l][j], stMax[r - (1 << j)][j])
                mn = min(stMin[l][j], stMin[r - (1 << j)][j])
                heappush(pq, (-(mx - mn), l, r - 1))
                
        return ans