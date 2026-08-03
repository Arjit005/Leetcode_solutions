from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # it is different from stone 1 , in stone one we have one choice but here we can choose m piles
        # he can take piles ,1 <= X <= 2*M, initially can take 1 

        #player 1 cannot take all piles unless there are only 1 or 2 piles remaining.

        #If the remaining piles are ≤ 2*M, the current player can take every remaining pile.

        #During the game: M grows as M = max(M, X).

        #suffix[i]=total stones from i to end ,Then after choosing X piles,
        #both index and M determine the future

        #Current player gets Remaining stones - Opponent stones
        n = len(piles)
        # suffix[i] = total stones from i to end
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]
        @cache
        def dp(i, M):

            # I can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            ans = 0

            # Try every possible X
            for X in range(1, 2 * M + 1):

                # My stones = Remaining stones − Opponent's stones
                my_stones = suffix[i] - dp(i + X, max(M, X))

                ans = max(ans, my_stones)

            return ans

        return dp(0, 1)
