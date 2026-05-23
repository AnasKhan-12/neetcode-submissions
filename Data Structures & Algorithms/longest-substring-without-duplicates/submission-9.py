class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=[]
        max_length=0
        for i in s:
            while i in window:
                window.pop(0)
            window.append(i)
            max_length=max(max_length, len(window))
        return max_length