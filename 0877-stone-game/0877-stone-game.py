from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
      #This is a two-player optimal game.  
      # recurrence==> immediate result + future result
      # my_advantage==> immediate gain-opponent's advantage
      # My final advantage = What I gain now − The advantage my opponent can achieve afterward.


      #dp(i,j) = maximum score difference the current player can achieve from piles[i...j].
        @cache
        def dp(i,j):
        # base case if only one element remains
            if i==j:
                return piles[i]
            left=piles[i]-dp(i+1,j)  # if i choose left element then  my adv
            right=piles[j]-dp(i,j-1) # if i choose right element then my adv
            return max(left,right)
        return dp(0, len(piles)-1)>0