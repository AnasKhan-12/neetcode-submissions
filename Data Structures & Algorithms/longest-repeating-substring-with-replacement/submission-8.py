class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        max_char=0
        length=0

        for i in range(len(s)):
            count[s[i]] = 1+count.get(s[i],0)
            max_char=max(max_char,count[s[i]])
            
            while (i-left+1) - max_char > k:
                count[s[left]]-=1
                left+=1
            length=max(length,i-left+1)
        return length
