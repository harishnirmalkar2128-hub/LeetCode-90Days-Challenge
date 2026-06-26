class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        # OFFSET helps us change negative sums into positive indexes (suchash) 🛠️
        OFFSET = n + 1
        
        # Fenwick Tree array to store counts of prefix sums
        bit = [0] * (2 * n + 2)
        
        def update(idx: int, val: int):
            while idx < len(bit):
                bit[idx] += val
                idx += idx & (-idx)
                
        def query(idx: int) -> int:
            total = 0
            while idx > 0:
                total += bit[idx]
                idx -= idx & (-idx)
            return total
        
        # Initially, the prefix sum is 0. We store its frequency.
        current_sum = 0
        update(current_sum + OFFSET, 1)
        
        result = 0
        
        for num in nums:
            # Change target to +1, and other numbers to -1
            if num == target:
                current_sum += 1
            else:
                current_sum -= 1
                
            # Query all previous prefix sums that are strictly less than current_sum
            result += query(current_sum + OFFSET - 1)
            
            # Add the current prefix sum to our Fenwick Tree
            update(current_sum + OFFSET, 1)
            
        return result