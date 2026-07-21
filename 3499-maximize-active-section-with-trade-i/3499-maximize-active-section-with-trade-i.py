class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        
        zero_blocks = []
        one_blocks = []
        
        i = 0
        n = len(t)
        
        initial_ones = s.count('1')
        
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            length = j - i
            
            if t[i] == '0':
                zero_blocks.append(length)
            else:
                one_blocks.append(length)
            i = j

        max_gain = 0
        for k in range(1, len(one_blocks) - 1):
            gain = zero_blocks[k - 1] + zero_blocks[k]
            max_gain = max(max_gain, gain)
            
        return initial_ones + max_gain