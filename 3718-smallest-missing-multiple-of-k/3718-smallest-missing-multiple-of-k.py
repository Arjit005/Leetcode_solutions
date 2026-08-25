class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        while i < len(nums)+2:
            if k*i not in nums:
                return k*i
            i=i+1
            
