class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #The digits are ordered from most significant to least significant in left-to-right order.

        #The large integer does not contain any leading 0's.

        #Increment the large integer by one and return the resulting array of digits.

        str_of_digit=''.join(map(str, digits))
        
        str_to_int=int(str_of_digit)

        increment_of_digit=str_to_int+1
        res=[]
        while increment_of_digit>0:
            res.append(increment_of_digit%10)
            increment_of_digit//=10
        res.reverse()  
        return res 



