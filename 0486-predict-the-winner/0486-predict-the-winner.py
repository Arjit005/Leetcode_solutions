from functools import lru_cache
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(left_end,right_end):
            # only one number is left 
            # and current player takes it 
            if left_end==right_end:
                return nums[left_end]
            #  Choice 1: Take the left number.
            # Opponent becomes the current player for the remaining subarray.    
            left_choice=nums[left_end]-dfs(left_end+1,right_end)

            # Choice 2: Take the right number.
            right_choice=nums[right_end]-dfs(left_end,right_end-1)
            # Current player chooses the move
            # that gives the maximum score difference.
            return max(left_choice,right_choice)
        
        # Initially, Player 1 is the current player.
        # If Player1 - Player2 >= 0,
        # Player 1 wins or ties.\
        return dfs(0,len(nums)-1)>=0