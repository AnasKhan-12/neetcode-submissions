class Solution:
    def isPalindrome(self, s: str) -> bool:

        # first make two pointers and helper function

        left=0
        right=len(s)-1

        while left < right:
        # move pointers only if there's a invalid character 
            while left < right and not self.isalphnum(s[left]): #if a invalid character then increment left pointer
                left+=1
            while right > left and not self.isalphnum(s[right]): #if a invalid character then decrement right pointer
                right-=1
       
        #------

        # if there's a valid character check whether they are equal or not
        # if not return false 
        # if they are equal move the pointers

            if s[left].lower() != s[right].lower():
                return False

            left,right = left+1,right-1
        return True

    def isalphnum(self,c):
            
        return (ord("A") <= ord(c) <= ord("Z") or
        # we cannot do ord("A") <= c <= z because A-Z includes some characters 
        #such as ' / ] as well and we dont want to include them so we deo A to Z 
        #and then again separately a to z
                ord("a") <= ord (c) <= ord ("z") or
                ord("0") <= ord(c) <= ord ("9")
                )
        