class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        for i in s:
            if i == "[":
                res.append("]")
            elif i == "{":
                res.append("}")
            elif i == "(":
                res.append(")")
            else:
                if not res or i != res[-1]:
                    return False
                else:
                    res.pop()
        if res:
            return False
        else:
            return True 