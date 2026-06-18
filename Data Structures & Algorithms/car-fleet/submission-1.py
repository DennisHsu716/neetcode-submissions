class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        stack = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            res.append((position[i], time))
        res.sort(reverse=True)
        for pol, time in res:
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
