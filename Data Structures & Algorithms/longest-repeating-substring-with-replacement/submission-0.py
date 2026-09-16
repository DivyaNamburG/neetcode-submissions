class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxfre = 0 
        maxlength = 0 
        left = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0)+ 1
            maxfre = max(maxfre,  count[s[right]])
            while (right - left + 1) - maxfre > k:
                count[s[left]] -= 1
                left += 1
            maxlength = max(maxlength, right - left + 1)
        return maxlength
