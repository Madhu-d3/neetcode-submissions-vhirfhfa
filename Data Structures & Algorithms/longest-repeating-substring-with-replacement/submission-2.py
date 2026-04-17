class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            # Is it valid
            if (i-l+1) -max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        return res
        