class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = False 
        second = False 
        third = False 

        for trip in triplets:
            if trip[0] > target[0] or trip[1] > target[1] or trip[2] > target[2]:
                continue 
            
            if trip[0] == target[0]:
                first = True 

            if trip[1] == target[1]:
                second = True 
            if trip[2] == target[2]:
                third = True
        
        return first and second and third