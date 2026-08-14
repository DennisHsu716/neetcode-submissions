class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        need = {}
        have = 0
        left = 0 
        res = ""
        len_res = float("inf")

        for i in t:
            need[i] = need.get(i, 0) + 1
        
        need_len = len(need)

        for i in range(len(s)):
            c = s[i]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1
            
            while have == need_len:
                if i - left + 1 < len_res:
                    len_res = i - left + 1
                    res = s[left:i + 1]
            
                out = s[left] 
                window[out] -= 1

                if out in need and window[out] < need[out]:
                    have -= 1
                left += 1
        return res 
                