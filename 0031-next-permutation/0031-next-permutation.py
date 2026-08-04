class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        #If no larger permutation exists, return the smallest permutation.

        # The next permutation of an array of integers is the next lexicographically greater permutation of its integer.

        #Permutations follow the same comparison rule—they're just limited to rearrangements of the same digits.

        # we have to ask simple question : What is the smallest arrangement that is bigger than 132? for specific case .its 213 like that we have to find next permutation.

        #The algorithm doesn't generate all permutations.
        #If you want the smallest possible increase, where should you try to make the change?  NEAR THE RIGHT DIGIT.

        #Changing the last digit changes the number much less than changing the first digit.
        #So the right side is where we should look first

        #The rule is:
        #Starting from the right, the first number that has a larger number somewhere to its right is the pivot.

        #In the algorithm, we don't sort this suffix. We simply reverse it.
        #i == -1 , What does that mean?
        #=>It means the array is completely decreasing, so it is already the largest permutation.

        #Think of it this way

        # Whenever you compare:

        # nums[i]
        # nums[i+1]


        # step 1==> find the pivot
                      
        i=len(nums)-2 # think you are comparing pairs, so you have to stop before 2 index to the end
        pivot=0
        while i>=0 and nums[i]>=nums[i+1]: #Not decreasing.STOP.
            i-=1 # we are decreasing i
            #Now you ask:  "Is this pair decreasing?"
            #i >= 0 We're literally asking: "Am I still standing inside the array? If yes, keep checking.If no,stop.
        
        if i==-1:
            nums.reverse()
            return
        j=len(nums)-1
        # Because the suffix is already decreasing, so the first number greater than the pivot that we meet from the right is exactly the one we want.
        while nums[j]<=nums[i]:
            j-=1
        
        # now swap nums[i] and nums[j]
        nums[i],nums[j]=nums[j],nums[i]# inpace swaping 

        # now reverse suffix
        left=i+1
        right=len(nums)-1
        while left<right:
            nums[left],nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        