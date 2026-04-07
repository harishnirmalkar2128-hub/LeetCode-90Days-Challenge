class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647
        
        
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
           
            res = res * 10 + digit
            
        res *= sign
        
        if res < MIN_INT or res > MAX_INT:
            return 0
            
        return res