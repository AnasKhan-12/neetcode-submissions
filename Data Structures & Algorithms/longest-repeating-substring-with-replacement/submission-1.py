class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        left = 0
        maxf = 0

        for right in range(len(s)):
            # right would act as our right pointer which will expan window

            count[s[right]] = 1 + count.get(s[right], 0) # if a char exists in dictionary add 1 to it...if it doesnt add it in dictionary and add 1 to it
           
            maxf = max(maxf, count[s[right]]) # max size of window

            while (right - left + 1) - maxf > k: # check window size - max repeating char <= k ....if greater than move left pointer
                count[s[left]] -= 1 # when left pointer moves decrement char frequency from dict
                left += 1 #to make the pointer now point to next char instead of the first
            result = max(result, right - left + 1)

        return result



        