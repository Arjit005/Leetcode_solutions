class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        # type hinting se ek chij samajh ati hai ki output ek integer chaiye

        # hme krna kya hai==> deletion of max and min element from array
        # deletion hoga form front ya back
        # return mininmum number if deletion , it would take to remove both element

        # problem ==> decide krna kha se remove karrenge 
        maximum_element=max(nums)
        minimum_element=min(nums)
        # Dono ke index find karo
        index_min = 0
        index_max = 0
        for i in range(len(nums)):
            if nums[i]==maximum_element:
                index_max=i
            if nums[i]==minimum_element:
                index_min=i    
        # Case 1: Dono front se remove
        front = max(index_min, index_max) + 1
        n=len(nums)
        # Case 2: Dono back se remove
        back = max(n - index_min, n - index_max)

        # Case 3: Minimum front se, maximum back se
        min_front_max_back = (index_min + 1) + (n - index_max)

        # Case 4: Maximum front se, minimum back se
        max_front_min_back = (index_max + 1) + (n - index_min)

        # Chaaro possibilities mein minimum answer
        return min(
            front,
            back,
            min_front_max_back,
            max_front_min_back
        )  

