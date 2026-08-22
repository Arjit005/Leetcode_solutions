class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_of_digit=0
        product_of_digit=1
        copy_of_integer=n
        while copy_of_integer>0:
            digit=copy_of_integer%10
            sum_of_digit+=digit
            product_of_digit*=digit
            copy_of_integer=copy_of_integer//10
        total_sum=sum_of_digit+product_of_digit   

        # check divisibility
        if n%total_sum==0:
            return True
        else:
            return False     


