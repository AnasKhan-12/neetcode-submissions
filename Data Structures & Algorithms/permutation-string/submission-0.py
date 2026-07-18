class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False
        
        def get_count(s):
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            return count
        
        s1_count = get_count(s1)
        window = get_count(s2[:k])
        
        if s1_count == window:
            return True
        
        for i in range(k, len(s2)):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - k]) - ord('a')] -= 1
            
            if window == s1_count:
                return True
        
        return False