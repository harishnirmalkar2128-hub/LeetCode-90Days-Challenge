from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)
        odd_char = ""
        half_counts = {}
        
        for char in sorted(count.keys()):
            cnt = count[char]
            if cnt % 2 != 0:
                if odd_char:
                    return ""
                odd_char = char
            if cnt // 2 > 0:
                half_counts[char] = cnt // 2

        half_len = sum(half_counts.values())

        ways = math.factorial(half_len)
        for cnt in half_counts.values():
            ways //= math.factorial(cnt)

        if ways < k:
            return ""

        left_half = []
        rem_len = half_len

        for _ in range(half_len):
            for ch in sorted(half_counts.keys()):
                if half_counts[ch] == 0:
                    continue
                
                next_ways = ways * half_counts[ch] // rem_len
                
                if k <= next_ways:
                    left_half.append(ch)
                    half_counts[ch] -= 1
                    ways = next_ways
                    rem_len -= 1
                    break
                else:
                    k -= next_ways

        left = "".join(left_half)
        return left + odd_char + left[::-1]