class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary for matching pairs
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            # Agar character closing bracket hai
            if char in bracket_map:
                # Stack se top element nikaalo agar stack khali nahi hai
                top_element = stack.pop() if stack else '#'
                
                # Check if matching partner is correct
                if bracket_map[char] != top_element:
                    return False
            else:
                # Agar opening bracket hai, toh stack mein push karo
                stack.append(char)
                
        # Last mein stack khali hona chahiye
        return not stack