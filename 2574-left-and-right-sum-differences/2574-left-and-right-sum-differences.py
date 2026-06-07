class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        total_sum = sum(nums)
        left_sum = 0
        answer = []
        
        for x in nums:
            right_sum = total_sum - left_sum - x
            answer.append(abs(left_sum - right_sum))
            left_sum += x
            
        return answer