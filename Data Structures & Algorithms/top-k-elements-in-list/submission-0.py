class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Step 1: Count frequencies
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Sort by frequency (descending)
        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        # Step 3: Return top k
        return sorted_nums[:k]

        