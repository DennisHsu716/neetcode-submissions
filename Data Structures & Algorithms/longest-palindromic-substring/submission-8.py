class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_long = 0

        for i in range(len(s)):
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            odd = right - left - 1

            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            even = right - left - 1

            length = max(odd, even)

            if length > max_long:
                max_long = length 
                if length == odd:
                    start = i - length // 2
                else:
                    start = i - length // 2 + 1
        return s[start:start + max_long] 