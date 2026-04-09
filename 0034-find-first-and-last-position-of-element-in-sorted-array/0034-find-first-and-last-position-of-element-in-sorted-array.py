class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst):
            low, high = 0, len(nums) - 1
            ans = -1
            
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    if isFirst:
                        high = mid - 1 
                    else:
                        low = mid + 1  
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        
        return [findBound(True), findBound(False)]