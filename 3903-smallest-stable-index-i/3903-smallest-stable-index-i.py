class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # An index i is called stable if its instability score is less than or equal to k.
        # Return the smallest stable index. If no such index exists, return -1.
        stable_index=[]
        for i in range(len(nums)):
            max_element=max(nums[:i+1])
            min_element=min(nums[i:])
            instability_score=max_element-min_element
            if instability_score<=k:
                stable_index.append(i)
                
        # check before its empty or not
        if stable_index:
            smallest_stable_index = min(stable_index)
            return smallest_stable_index
        else:
            return -1    
