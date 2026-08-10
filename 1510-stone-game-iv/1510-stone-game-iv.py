class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                if not dp[i - j * j]:  # Found a losing position for opponent!
                    dp[i] = True
                    break
                j += 1
        
        return dp[n]