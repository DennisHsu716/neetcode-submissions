class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                a = ord(num1[i]) - ord('0') 
                b = ord(num2[j]) - ord('0')

                digit = a * b

                pos1 = i + j
                pos2 = i + j + 1

                res[pos2] += digit
                res[pos1] += res[pos2] // 10
                res[pos2] %= 10
        
        start = 0
        while start < len(res) - 1 and res[start] == 0:
            start += 1
        return ''.join(str(x) for x in res[start:]) 