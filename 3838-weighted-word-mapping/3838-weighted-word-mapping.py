from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        
        for word in words:
            # Step 1: Word ke saare characters ka total weight calculate karenge
            total_weight = sum(weights[ord(char) - ord('a')] for char in word)
            
            # Step 2: Total weight ka modulo 26 lenge
            rem = total_weight % 26
            
            # Step 3: Reverse alphabetical order mein map krenge (0 -> 'z', 1 -> 'y', ..., 25 -> 'a')
            mapped_char = chr(ord('z') - rem)
            
            result.append(mapped_char)
            
        # Step 4: Saare characters ko join karke final string return karenge
        return "".join(result)