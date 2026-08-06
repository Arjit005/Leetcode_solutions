class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # return number greater than or equal to n , which digit product is divisible by t
        prod=1
        n1=n # so that original value not destroy
        while n1 > 0:
            digit = n1 % 10   # Extract last digit

            # Do something with digit
            prod=prod*digit
            n1 //= 10         # Remove last digit
        if prod % t==0:
            return n
        else:
                # n=n+1 
                return self.smallestNumber(n+1,t)    # calling that function again until i get result i wanted