class Solution:
    def rob(self, nums: List[int]) -> int:
        def houses(house):
            n = len(house)
            if n == 1:
                return house[0]
            dp = [0] * n
            dp[0] = house[0]
            dp[1] = max(house[0], house[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + house[i])
            return dp[n - 1]
        if len(nums) == 1:
            return nums[0]
        case1 = houses(nums[1:])
        case2 = houses(nums[:-1])
        return max(case1, case2)
        