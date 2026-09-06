class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[j] will store the number of ways to form t[0..j-1]
        dp = [0] * (len(t) + 1)
        dp[0] = 1  # Base case: 1 way to form an empty string
        
        # Map each character in t to its indices (stored in descending order)
        t_indices = {}
        for j in range(len(t) - 1, -1, -1):
            char = t[j]
            if char not in t_indices:
                t_indices[char] = []
            t_indices[char].append(j)
            
        # Iterate through each character in s
        for char in s:
            if char in t_indices:
                # Update DP array backwards to use values from the previous "row"
                for j in t_indices[char]:
                    dp[j + 1] += dp[j]
                    
        return dp[-1]