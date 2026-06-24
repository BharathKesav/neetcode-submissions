class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: s1 cannot be larger than s2
        if len(s1) > len(s2):
            return False
            
        h1 = [0] * 26
        h2 = [0] * 26
        
        # Populate the frequency array for s1
        for char in s1:
            h1[ord(char) - ord('a')] += 1
            
        j = 0
        for i in range(len(s2)):
            # 1. Add the current character to the window
            h2[ord(s2[i]) - ord('a')] += 1
            
            # 2. Shrink the window from the left if it exceeds the length of s1
            if i - j + 1 > len(s1):
                h2[ord(s2[j]) - ord('a')] -= 1
                j += 1
                
            # 3. Check for a match AFTER the window has been properly updated
            if h1 == h2:
                return True
                
        return False