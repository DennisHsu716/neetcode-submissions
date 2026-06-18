class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        text = []
        for i in s:
            if i.isalnum():
                text.append(i)
        l = 0
        r = len(text) - 1
        while l <= r:
            if text[l] != text[r]:
                return False 
            else:
                l += 1
                r -= 1
        return True 