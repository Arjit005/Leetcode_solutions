class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # apply xor operation in longest sunsequence 
        # first task is to find the subsequence then we will apply  bitwise XOR operations
        # we have to figure out element of subsequence
        # codition is we have to return the ""length of longest subsequence"" whose XOR is non zero
        """
        Calculate XOR of entire array
            ↓
        XOR != 0?
        /       \
        YES        NO
        ↓          ↓
    n   Is there a non-zero element?
                /       \
                YES        NO
                ↓          ↓
            n - 1        0

        """
        #A subsequence does not have to be contiguous.
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        if xor_all != 0:
            return len(nums)
        else:
            if all(num == 0 for num in nums):
                return 0
            else:
                return len(nums) - 1






