class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:

        """
        Chunk 2: Why parity (odd/even) is the only thing that matters

        An even number is divisible by 2 → remainder 0
        An odd number is not → remainder 1

        The final array only cares about these remainders.
        """
        #You only need to decide if it is possible.
        # find minimum element 
        minimum_element=min(nums1)
        has_even=False
        has_odd=False

        for x in nums1:
            if x%2==1:
                has_odd=True
            else:
                has_even=True    

        if not has_even or not has_odd:
            return True 
        return minimum_element%2==1
        