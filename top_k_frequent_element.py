
class Solution:
    def topKFrequent(self, nums, k):
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        sorted_nums = sorted(
            frequency,
            key=frequency.get,
            reverse=True
        )

        return sorted_nums[:k]
