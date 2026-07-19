class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for i in range(len(s)):
            if s[i] == "(":
                res.append(")")
            elif s[i] == "[":
                res.append("]")
            elif s[i] == '{':
                res.append("}")
            else:
                if not res or s[i] != res[-1]:
                    return False 
                res.pop()
        if len(res) != 0:
            return False 
        else:
            return True 