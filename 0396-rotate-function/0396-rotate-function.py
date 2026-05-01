class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        f = sum(i * nums[i] for i in range(n))

        max_val = f

        for k in range (1, n):
            f = f + s - n * nums[n - k]
            if f > max_val:
                max_val = f

        return max_val