class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={")":"(","}":"{","]":"["}
        # mapping should be from closing brackets
        # because in our input we will take all the opening brackets into our stack
        # then we will check them from the remaining closing brackets of input
        # thats why mapping: closing -> opening
        for i in s:
            if i in mapping:
                if stack and stack[-1] == mapping[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
