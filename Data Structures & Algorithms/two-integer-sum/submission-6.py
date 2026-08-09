class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}

        for i in range(len(nums)):
            hash_map[nums[i]]=i

        for i,n in enumerate(nums):
            diff=target-n

            if diff in hash_map and i != hash_map[diff]:
                return [i,hash_map[diff]]