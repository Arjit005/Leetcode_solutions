class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        """The goal is to determine whether it's possible to plant a given number of flowers (denoted by n) in an existing flowerbed, subject to the constraint that no two flowers can be planted in adjacent plots."""

        for i in range(len(flowerbed)):
            # Check left neighbor
            left = 0 if i == 0 else flowerbed[i - 1]

            # Check right neighbor
            right = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]
            current=flowerbed[i]
            if current==0 and left ==0 and right==0:
                    # plant flower 
                    flowerbed[i]=1
                    n=n-1


            if n<=0:
                    return True
        return False