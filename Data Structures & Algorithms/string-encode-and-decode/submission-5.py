class Solution:

    def encode(self, strs: List[str]) -> str:
        group = ""
        for i in range(len(strs)):
            # len + # + i
            group += str(len(strs[i])) + "#" + strs[i]
        return group

    def decode(self, s: str) -> List[str]:
        #j=i
        #j to find # and i 
        #res
        #lengthe and word
        res = []
        i = 0
        while i < len(s):
            j = i
            if s[j] != "#":
                j += 1
            length = int(s[i:j]) 
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 + length
        return res 
