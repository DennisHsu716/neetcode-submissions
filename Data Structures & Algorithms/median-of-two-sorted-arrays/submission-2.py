class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1 
        B = nums2

        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = (total + 1) // 2

        l = 0 
        r = len(A)

        while l <= r:
            i = (l + r) // 2
            j = half - i

            aleft = A[i-1] if i > 0 else float("-inf")
            aright = A[i] if i < len(A) else float("inf")

            bleft = B[j-1] if j > 0 else float("-inf")
            bright = B[j] if j < len(B) else float("inf")

            if aleft <= bright and bleft <= aright:
                if total % 2 == 1:
                    return max(aleft, bleft)
                return (max(aleft, bleft) + min(aright, bright)) / 2

            elif aleft < bright:
                r = j - 1
            else:
                l = i + 1
            

