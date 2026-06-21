class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #A < B
        A = nums1
        B = nums2
        if len(A) > len(B):
            A, B = B, A
        total = len(A) + len(B)
        half = (total + 1) // 2
        #l < r f
        l = 0
        r = len(A)
        #i and j, aleft, aright, bleft, bright
        while l <= r:
            i = (l + r) // 2 
            j = half - i

            aleft = A[i - 1] if i > 0 else float("-inf")
            aright = A[i] if i < len(A) else float("inf")

            bleft = B[j - 1] if j > 0 else float("-inf")
            bright = B[j] if j < len(B) else float("inf")
        #aleft < bright, bleft < aright
        #return maxleft or return left + right / 2
            if aleft <= bright and bleft < aright:
                if total % 2 == 1:
                    return max(aleft, bleft)
                return (max(aleft, bleft) + min(aright, bright)) / 2
        #i + 1 or j - 1
            elif aleft > bright:
                r = j - 1
            else:
                l = i + 1
