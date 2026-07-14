class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={}

        for i in range(len(nums)):
            indices[nums[i]]=i


        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]] 
                # the main thing is you are returning the difference's indice directly
                # and then also checking if that difference exists in dictionary
                # so obviously it exists and it exists with the same indice as you are currently at
                # to avoid returning the same indice we do the check for !=i 
        return []