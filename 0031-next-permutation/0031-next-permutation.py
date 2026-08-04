class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        # Goal:
        # Rearrange nums into the next lexicographically greater permutation.
        # If no greater permutation exists, transform it into the smallest one.

        # Key Idea:
        # Increase the number as late as possible (from the right),
        # by as little as possible, then make everything after it
        # as small as possible.

        # -------------------------------------------------------
        # Step 1: Find the pivot.
        # Scan from the right and find the first index where:
        # nums[i] < nums[i+1]
        #
        # Everything to the right of this pivot is already
        # in decreasing order.
        # -------------------------------------------------------

        i = len(nums) - 2

        # Keep moving left while the current pair is decreasing.
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # No pivot means the whole array is decreasing.
        # It is already the largest permutation,
        # so return the smallest permutation.
        if i == -1:
            nums.reverse()
            return

        # -------------------------------------------------------
        # Step 2: Find the successor.
        # Find the smallest element greater than nums[i].
        #
        # Since the suffix is decreasing, scanning from the
        # right guarantees the first valid element is the answer.
        # -------------------------------------------------------

        j = len(nums) - 1

        while nums[j] <= nums[i]:
            j -= 1

        # -------------------------------------------------------
        # Step 3: Swap pivot and successor.
        # This creates the next larger permutation.
        # -------------------------------------------------------

        nums[i], nums[j] = nums[j], nums[i]

        # -------------------------------------------------------
        # Step 4: Reverse the suffix.
        #
        # The suffix is currently in decreasing order.
        # Reversing it makes it increasing, producing the
        # smallest possible suffix.
        # -------------------------------------------------------

        left = i + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1