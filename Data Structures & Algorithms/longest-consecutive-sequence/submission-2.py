class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longests = 0
        for num in nums:
            if num - 1 not in numset:
                currentnum = num
                currents = 1
                while currentnum + 1 in numset:
                    currentnum += 1 
                    currents += 1
                longests = max(longests, currents)
        return longests