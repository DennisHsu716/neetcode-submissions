class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        for i in range(len(s)):
            if s[i] == t[i]:
                i += 1
            else:
                return False 
        return True 

        