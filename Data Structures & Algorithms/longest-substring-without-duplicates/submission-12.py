class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char=set()
        left=0
        maxstring=0

        # for i in s:
        #     while i in char:
        #         char.remove(i)
        #     char.add(i)
            # maxstring= we need i as a index here for calculating length

        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[left]) # not s[i] because it will only remove that specific element and we want to remove elements UPTO the repeating element
                left+=1
            char.add(s[i])
            maxstring=max(maxstring,i-left+1)
        return maxstring