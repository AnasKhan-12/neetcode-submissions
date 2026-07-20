class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output=[0]*len(temperatures)
        stack=[]

        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                stack_temp,temp_index=stack.pop()
                output[temp_index] = i-temp_index
            stack.append((n,i))
        return output