class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        if len(nums) != n + 1:
            return False

        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1

        for i in range(1, n):
            if count.get(i) != 1:
                return False

        return count.get(n) == 2