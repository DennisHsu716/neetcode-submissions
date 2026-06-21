class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #count, left, res
        count = {}
        left = 0 
        res = 0 
        max_freq = 0

        for i in range(len(s)):
            n = s[i]
            count[n] = count.get(n, 0) + 1
            max_freq = max(max_freq, count[n]) 

        #count get s -> max freq
        #compare to k, 
            while (i - left + 1) - max_freq > k:
                count[n] -= 1
                left += 1

            res = max(res, i - left + 1)
        return res