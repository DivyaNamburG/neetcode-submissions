class Solution:
    def climbStairs(self, n: int) -> int:
        dp1 = 1
        dp2 = 1
        for i in range(n - 1):
            dp = dp1 + dp2
            dp2 = dp1
            dp1 = dp
        return dp1
