class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        window = {}
        left = 0 

        for i in range(len(s1)):
            count[s1[i]] = count.get(s1[i], 0) + 1
        
        for i in range(len(s2)):
            window[s2[i]] = window.get(s2[i], 0) + 1

            if i - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            
            if count == window:
                return True 
        return False 