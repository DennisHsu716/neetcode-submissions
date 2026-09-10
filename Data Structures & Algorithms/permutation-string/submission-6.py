class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = {}
        window = {}
        left = 0 

        for i in range(len(s1)):
            res[s1[i]] = res.get(s1[i], 0) + 1
        
        for i in range(len(s2)):
            window[s2[i]] = window.get(s2[i], 0) + 1

            if (i - left + 1) > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            
            if res == window:
                return True 
        return False 