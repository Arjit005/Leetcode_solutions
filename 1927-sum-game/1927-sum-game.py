class Solution:
    def sumGame(self, num: str) -> bool:
        #Alice always goes first.
        #On their turn, a player picks exactly one ? anywhere on the board and replaces it with any digit from 0 to 9. They keep taking turns until there are no more question marks left.


        """    
        The Winning Conditions
        
        This is a game of balance versus chaos:

        Bob (The Balancer): Bob wins if, at the very end of the game, the sum of all digits on the left half is exactly equal to the sum of all digits on the right half.

        Alice (The Chaos-Maker): Alice wins if the left sum and the right sum are different.
        
        """
        # set up variable 
        sum_left=0
        sum_right=0
        q_left=0
        q_right=0
        # if q_left+q_right== odd , alice win--> because she gets last move ,return true 

        for i in range(len(num)//2):
            if num[i]=='?':
                q_left+=1
            else:    
                sum_left+=int(num[i])
        for i in range(len(num)//2,len(num)):
            if num[i]=='?':
                q_right+=1
            else:
                sum_right+=int(num[i])    

        if (q_left+q_right)%2!=0:  # means odd
            return True

        else:
            pairs=(q_right-q_left)/2
            points_from_q=pairs*9
            difference=sum_left-sum_right
            if points_from_q==difference:
                return False
            else:
                 return True
