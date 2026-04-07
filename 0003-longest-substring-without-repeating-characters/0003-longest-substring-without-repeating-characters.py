class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # Agar character repeat hua aur woh current window ke andar hai
            if s[right] in char_map and char_map[s[right]] >= left:
                # Left pointer ko repeat character ke next position par shift karein
                left = char_map[s[right]] + 1
            
            # Character ka naya index update karein
            char_map[s[right]] = right
            
            # Window ki length calculate karke max update karein
            max_length = max(max_length, right - left + 1)
            
        return max_length