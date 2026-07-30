class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return 
            
            for end in range(start, len(s)):
                sub = s[start:end+1]

                def isPal(sub):
                    left = 0
                    right = len(sub) - 1

                    while left < right:
                        if sub[left] != sub[right]:
                            return False 
                        left += 1
                        right -= 1
                    return True
                
                if not isPal(sub):
                    continue 
                
                path.append(sub)
                backtrack(end + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res 
