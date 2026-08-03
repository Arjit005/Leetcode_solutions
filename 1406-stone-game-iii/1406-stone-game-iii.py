from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # dp[i] = maximum score difference (current player - opponent)
        # starting from index i
        dp = [0] * (n + 1)

        # Fill from the end
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            curr_sum = 0

            # Take 1, 2, or 3 stones
            for j in range(i, min(i + 3, n)):
                curr_sum += stoneValue[j]
                best = max(best, curr_sum - dp[j + 1])

            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"