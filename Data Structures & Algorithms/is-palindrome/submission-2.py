class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        count = []
        for i in s:
            if i.isalnum():
                count.append(i)
        
        left = 0
        right = len(count) - 1

        while left < right:
            if count[left] == count[right]:
                left += 1
                right -= 1
            else:
                return False 
        return True 