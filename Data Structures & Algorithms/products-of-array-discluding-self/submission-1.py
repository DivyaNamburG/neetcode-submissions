class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        leftp = 1
        for i in range(n):
            output[i] = leftp
            leftp *= nums[i]
        rightp = 1
        for i in range(n-1, -1, -1):
            output[i] *= rightp
            rightp *= nums[i]
        return output
