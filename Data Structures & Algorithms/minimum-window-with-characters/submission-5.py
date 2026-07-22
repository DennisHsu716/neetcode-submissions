class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        left = 0
        have = 0
        res = ""
        res_len = float("inf")

        for i in t:
            need[i] = need.get(i, 0) + 1
        
        len_need = len(need)

        for i in range(len(s)):
            c = s[i]
            window[c] = window.get(c, 0) + 1

            if c in need and need[c] == window[c]:
                have += 1
            
            while have == len_need:
                if i - left + 1 < res_len:
                    res_len = i - left + 1
                    res = s[left:i + 1]
            
                i_out = s[left]
                window[i_out] -= 1

                if i_out in need and window[i_out] < need[i_out]:
                    have -= 1
                left += 1
        return res 