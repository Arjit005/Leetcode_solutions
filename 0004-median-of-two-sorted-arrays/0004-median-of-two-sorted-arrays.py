class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_list=nums1+nums2
        sorted_list=sorted(final_list)
        # finding median in mathematical way
        n=len(sorted_list)
        if n%2==1: # odd lenght 
            return float(sorted_list[n//2])
        
        else:
            return float(sorted_list[n//2-1]+sorted_list[n//2])/2


        
