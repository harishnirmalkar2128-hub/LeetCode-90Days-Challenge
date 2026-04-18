class Solution:
    def mirrorDistance(self, n: int) -> int:
        s = str(n)
        reversed_s = s[::-1] 
        reversed_n = int(reversed_s)
        
        res = n - reversed_n
        if res < 0:
            res = -res
            
        return res