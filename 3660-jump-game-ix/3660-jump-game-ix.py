from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # prefix maximum
        preMax = [0] * n
        preMax[0] = nums[0]

        for i in range(1, n):
            preMax[i] = max(preMax[i - 1], nums[i])

        ans = [0] * n
        sufMin = float('inf')

        # traverse from right to left
        for i in range(n - 1, -1, -1):

            if i < n - 1 and preMax[i] > sufMin:
                ans[i] = ans[i + 1]
            else:
                ans[i] = preMax[i]

            sufMin = min(sufMin, nums[i])

        return ans