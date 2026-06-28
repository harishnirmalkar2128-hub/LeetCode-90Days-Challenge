class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        # Step 1: Sort the array first
        arr.sort()
        
        # Step 2: The first element must be 1
        arr[0] = 1
        
        # Step 3: Loop through the array and apply the condition
        for i in range(1, len(arr)):
            # The next element can be at most 1 greater than the previous element
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
                
        # Step 4: The last element will be the maximum value
        return arr[-1]