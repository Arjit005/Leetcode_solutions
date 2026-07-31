class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # first bracket must be "("
        # At any point while building the string, the number of ) can never be greater than the number of (.
        # we need something to store results
        output=[]
        # we use backtrackin 
        # defining dfs
        def dfs(current,open_bracket,close_bracket): # current is string of brackets
            # base case
            if len(current)==2*n:
                output.append(current)
                return
            if open_bracket<n:
                dfs(current+"(",open_bracket+1,close_bracket)
            if close_bracket <open_bracket:#number of ) can never be greater than the number of (.
                dfs(current+")",open_bracket,close_bracket+1)
        dfs("",0,0) # starting point of tree
        return output
            
