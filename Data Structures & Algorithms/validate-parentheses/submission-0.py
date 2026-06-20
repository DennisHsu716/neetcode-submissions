class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            if s[i] == "[":
                res.append("]")
            elif s[i] == "(":
                res.append(")")
            elif s[i] == "{":
                res.append("}")
            elif s[i] == "]":
                res.remove("]")
            elif s[i] == "}":
                res.remove("}")
            else:
                res.remove(")")

        for j in res:
            if res != []:
                return False 
        return True 
            