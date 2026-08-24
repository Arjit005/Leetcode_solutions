class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        """
        What you are missing is the phrase "play optimally" from the problem description.

        Alice and Bob aren't just picking stones randomly or following a set pattern (like always starting or always ending). They are playing like supercomputers that can see the entire future of the game
        """
        # optimal--> dynamic programming
        n = len(stones)
        
        # Step 1: Calculate the prefix sums
        # prefix[i] represents the sum of stones from index 0 to i
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]
            
        # Step 2: Set the Base Case (The Final Move)
        # If Alice takes all the stones, she gets prefix[-1] and Bob gets 0.
        # So the score difference is exactly prefix[-1].
        best_difference = prefix[-1]
        
        # Step 3: Work backward to find optimal choices
        # We start at n-2 and go down to 1.
        # We stop at index 1 because you MUST take at least 2 stones (index > 0).
        for i in range(n - 2, 0, -1):
            # The optimal choice:
            # max( Skip and keep the current best , Take now and subtract opponent's future best )
            best_difference = max(best_difference, prefix[i] - best_difference)
            
        # Step 4: Return the maximum score difference Alice can guarantee
        return best_difference