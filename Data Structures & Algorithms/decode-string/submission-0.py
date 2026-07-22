class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        currentstring=""
        curnum=0
        for i in s:
            if i.isdigit():
                curnum= curnum * 10 + int(i)
            elif i == "[":
                stack.append((currentstring,curnum)) # ?? 
                curnum=0
                currentstring=""
            elif i == "]":
                prevstr,num=stack.pop()
                currentstring=prevstr + num*currentstring
            else:
                currentstring+=i
        return currentstring     