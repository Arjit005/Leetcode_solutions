from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        # We only care about each stone's remainder modulo 3.
        cnt0 = cnt1 = cnt2 = 0

        for s in stones:

            # Stone contributes 0 modulo 3.
            if s % 3 == 0:
                cnt0 += 1

            # Stone contributes 1 modulo 3.
            elif s % 3 == 1:
                cnt1 += 1

            # Stone contributes 2 modulo 3.
            else:
                cnt2 += 1


        # Case 1:
        # Even number of 0-stones.
        #
        # The 0-stones effectively preserve the turn structure,
        # so Alice needs to have access to both remainder-1
        # and remainder-2 stones.
        if cnt0 % 2 == 0:
            return cnt1 > 0 and cnt2 > 0


        # Case 2:
        # Odd number of 0-stones.
        #
        # Now the winner depends on how unbalanced the numbers
        # of remainder-1 and remainder-2 stones are.
        #
        # A difference of 0, 1, or 2 is not enough.
        # Alice wins only when the difference is greater than 2.
        return abs(cnt1 - cnt2) > 2