class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        have = 0
        left = 0
        res = ""
        res_len = float("inf")
        #need
        for i in t:
            need[i] = need.get(i, 0) + 1
        
        need_len = len(need)
        #window 

        for i in range(len(s)):
            c = s[i]
            window[c] = window.get(c, 0) + 1
        #have = len(need) -> update res
            if c in need and window[c] == need[c]:
                have += 1

            while have == need_len:
                if i - left + 1 < res_len:
                    res_len = i - left + 1
                    res = s[left: i + 1]

        #out -> left
                out = s[left]
                window[out] -= 1

                if out in need and window[out] < need[out]:
                    have -= 1
                left += 1
        return res  