class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndex = {}
        left = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] in charIndex:
                left = max(left, charIndex[s[i]]+1)
            charIndex[s[i]] = i
            max_length = max(max_length, i - left + 1)
        return max_length