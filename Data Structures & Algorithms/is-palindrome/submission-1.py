class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        count = []
        for i in s:
            if i.isalnum():
                count.append(i)
        
        l = 0
        r = len(count) - 1

        while l < r:
            if count[l] != count[r]:
                return False 
            else:
                l += 1
                r -= 1
        return True 

        