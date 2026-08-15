class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        """
        So our reasoning so far is:

                  Want maximum length
                         ↓
                  Try largest: n
                         ↓
              Calculate whole-array XOR
                         ↓
               ┌─────────┴─────────┐
               ↓                   ↓
            non-zero              zero
               ↓                   ↓
          answer = n          n is impossible
                                   ↓
                         Try next largest: n-1
        """

        """
        The key point is:

        XOR does not operate on decimal digits.
        It operates on the binary representation of the numbers.

        means it is converting decimal into binary then finding xor

        Same → 0, different → 1


                Want maximum length
                         ↓
                  Maximum = n
                         ↓
              Calculate total XOR
                    /         \
                   /           \
             non-zero           zero
                ↓                ↓
             answer n       n is impossible
                                  ↓
                         Investigate n - 1
                                  ↓
                      n - 1 = remove one
                                  ↓
                       Is there x != 0?
                           /          \
                         YES           NO
                          ↓             ↓
                  remove x          all zeros
                          ↓             ↓
                remaining XOR=x     impossible
                          ↓             ↓
                      n - 1            0
        """

        # A subsequence does not have to be contiguous,
        # but maintains relative order.

        """
        Suppose:

        nums = [0, 0, 0]

        This:

        num == 0 for num in nums

        checks every element.

        It effectively produces:

        0 == 0 → True
        0 == 0 → True
        0 == 0 → True

        So conceptually:

        all([True, True, True])

        all() asks:

        Are ALL of these True?
        """

        """
        Assume:
            total XOR = 0

        Choose a non-zero element x.

        whole XOR:

            x ^ remaining = 0

        Therefore:

            remaining = x

        Since:

            x != 0

        Therefore:

            remaining != 0

        So:

            length n - 1 is achievable.

        And:

            length n is impossible because total XOR = 0.

        Therefore:

            maximum length = n - 1.
        """

        """
                     Problem
                       │
            ┌──────────┴──────────┐
            ↓                     ↓
    "maximum length"          XOR = 0
            ↓                     ↓
    n is largest            remove x
            ↓                     ↓
    n fails              remaining XOR = x
            ↓                     ↓
    next candidate = n-1     if x ≠ 0 → valid
            └──────────┬──────────┘
                       ↓
                   answer n-1
        """

        # Calculate the XOR of the whole array.
        xor_all = 0

        for num in nums:
            xor_all ^= num

        # If the whole-array XOR is non-zero,
        # the whole array itself is the longest valid subsequence.
        if xor_all != 0:
            return len(nums)

        # If the total XOR is zero and every element is zero,
        # then every possible subsequence also has XOR = 0.
        if all(num == 0 for num in nums):
            return 0

        # Otherwise:
        #
        # total XOR = 0
        # but at least one element x is non-zero.
        #
        # Remove that non-zero element.
        # The remaining XOR becomes x, which is non-zero.
        #
        # Therefore, length n - 1 is achievable.
        return len(nums) - 1