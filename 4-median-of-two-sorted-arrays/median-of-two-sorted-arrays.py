class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        mer=nums1+nums2
        mer.sort()
        n=len(mer)
        if(n%2 == 0):
            res=mer[(n//2)-1]+mer[(n//2)]
            return res/2
        else:
            return float(mer[n//2])

