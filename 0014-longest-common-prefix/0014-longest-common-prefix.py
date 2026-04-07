class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Step 1: Base case handle karein
        if not strs:
            return ""
        
        # Step 2: Strings ko sort karein
        strs.sort()
        
        # Pehli aur aakhri string uthayein
        first = strs[0]
        last = strs[-1]
        ans = ""
        
        # Step 3: Dono ko compare karein
        # Jitna match karega, wahi hamara prefix hai
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
            
        return ans