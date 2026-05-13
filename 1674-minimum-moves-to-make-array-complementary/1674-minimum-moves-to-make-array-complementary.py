class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit

            diff[2] += 2
            diff[low] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[high + 1] += 1

        res = n
        curr = 0
        for i in range(2, 2 * limit + 1):
            curr += diff[i]
            res = min(res, curr)
            
        return res