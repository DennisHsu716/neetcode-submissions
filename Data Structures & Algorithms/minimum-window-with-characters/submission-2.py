class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        need = {}
        left = 0
        have = 0
        res = ""
        res_len = float("inf")

        for i in t:
            need[i] = need.get(i, 0) + 1
        
        need_len = len(need)

        for i in range(len(s)):
            c = s[i]
            window[c] = window.get(c, 0) + 1

            #c -> window == need 
            if c in need and window[c] == need[c]:
                have += 1

            #have == need_len
            while have == need_len:
                if i - left + 1 < res_len:
                    res_len = i - left + 1
                    res = s[left:i + 1]
 
            #out 
                out = s[left]
                window[out] -= 1
                
                if out in need and window[out] < need[out]:
                    have -= 1
                left += 1
        return res
