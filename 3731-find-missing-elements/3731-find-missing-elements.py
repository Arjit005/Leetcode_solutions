class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # goal==>
        # return all integers which are missing in inside  sorted list. 
        # if nothing returs then return empty list  

        #  ==> i am going  find smallest and largest element of given array 
        smallest_element = min(nums)
        largest_element=max(nums)
        result=[]
        for i in range(smallest_element,largest_element+1):
            if i not in nums:
                result.append(i)
            
        result.sort()
        return result         

