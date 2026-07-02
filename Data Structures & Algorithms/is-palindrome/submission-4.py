class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        text = [] 
        for i in s:
            if i.isalnum():
                text.append(i)
        
        left = 0
        right = len(text) - 1

        while left < right:
            if text[left] == text[right]:
                left += 1
                right -= 1
            else:
                return False 
        return True 
        

