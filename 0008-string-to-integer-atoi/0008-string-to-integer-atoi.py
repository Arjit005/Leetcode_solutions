class Solution:
    def myAtoi(self, s: str) -> int:
        # a to i ==> str to integer without using  int() fun
        i=0
        n=len(s)
        sign=1
        num=0
        while i <n and s[i]==' ':  # skip spaces
            i=i+1
        if i<n:    
            if s[i]=='-':
                sign=-1
                i=i+1
            elif s[i]=='+':
                i=i+1

        while i<n and s[i].isdigit():
                digit = int(s[i])
                num = num * 10 + digit    
                i=i+1
        num *= sign  
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if num > INT_MAX:
            return INT_MAX

        if num < INT_MIN:
            return INT_MIN

        return num  
          