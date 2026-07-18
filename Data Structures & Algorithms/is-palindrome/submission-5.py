class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = []
        for i in s:
            if i.isalnum():
                res.append(i)
        
        left = 0
        right = len(res) - 1

        while left < right:
            if res[left] == res[right]:
                left += 1
                right -= 1
            else:
                return False 
        return True 