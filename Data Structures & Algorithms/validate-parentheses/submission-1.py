class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            if s[i] == "[":
                res.append("]")
            elif s[i] == "(":
                res.append(")")
            else:
                res.append("}")

            if i == "]":
                if not res and res[-1] != "[":
                    return False 
                res.pop()
            elif i == ")":
                if not res and res[-1] != "(":
                    return False 
                res.pop()
            else:
                if not res and res[-1] != "{":
                    return False 
                res.pop()
        if len(res) != 0:
            return False 
        else:
            return True 
            