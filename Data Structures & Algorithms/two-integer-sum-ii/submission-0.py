class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(numbers)):
            if numbers[i] not in hash:
                # hash[numbers[i]]=1+hash.get(numbers[i],0)
                hash[numbers[i]]=i
            
            diff=target-numbers[i]
            if diff in hash and hash[diff] != i:
                return sorted([i+1,hash[diff]+1])
                