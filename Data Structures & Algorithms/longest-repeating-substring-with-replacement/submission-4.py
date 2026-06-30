class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        left = 0
        res = 0 
        max_freq = 0 

        for i in range(len(s)):
            c = s[i]
            window[c] = window.get(c, 0) + 1
            max_freq = max(max_freq, window[c])

            while (i - left + 1) - max_freq > k:
                window[s[left]] -= 1
                left += 1
            
            res = max(res, i - left + 1)
        return res 