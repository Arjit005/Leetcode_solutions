class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        """
        ┌──────────────────────┐
        │  Find sequential     │
        │       prefix         │
        └──────────┬───────────┘
                   ↓
              Calculate sum
                   ↓
             Start at sum
                   ↓
            Is x in nums?
              ↙         ↘
            YES          NO
             ↓            ↓
           x + 1       RETURN x
             │
             └──────────→

   """
        # it is understood that len of nums is greater than 1
        prefix_sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                prefix_sum+=nums[i]
            else:
                break
        
        x=prefix_sum # ek condtion jo ki while loop ke liye necessary hoti hai

        while x in nums:
            x=x+1
        return x     
