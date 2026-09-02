class CountSquares:

    def __init__(self):
        self.point = {}
        

    def add(self, point: List[int]) -> None:
        x, y = point 
        
        self.point[(x, y)] = self.point.get((x, y), 0) + 1

    def count(self, point: List[int]) -> int:
        x, y = point 
        res = 0

        for (px, py) in self.point:
            if py != y:
                continue 
            
            d = abs(x - px)

            top_left = (x, y + d)
            top_right = (px, y + d) 

            botton_left = (x, y - d)
            botton_right = (px, y - d)

            res += (
                self.point.get(top_left, 0) * 
                self.point.get(top_right, 0) *
                self.point.get((px, py), 0)
            )

            res += (
                self.point.get(botton_left, 0) * 
                self.point.get(botton_right, 0) *
                self.point.get((px, py), 0)
            )
        return res 


        
