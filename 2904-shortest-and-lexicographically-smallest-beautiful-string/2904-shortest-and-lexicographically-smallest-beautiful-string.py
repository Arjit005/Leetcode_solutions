# from collections import Counter
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        #A substring of s is beautiful if the number of 1's in it is exactly k.
        # substring => continuous
        # there is no  ones then return empty string 
        count_ones=0
        for i in range(len(s)):
            if s[i]=="1":
                count_ones+=1
        if count_ones<k:
            return ""


        """
                total ones
                    │
          ┌─────────┴─────────┐
          │                   │
       < k                   >= k
          │                   │
       return ""          find candidate
                              │
                    ┌─────────┴─────────┐
                    │                   │
                 == k                  > k
                    │                   │
               shrink ends        examine groups
        """
        ones=[]
        for i in range(len(s)):
            if s[i]=="1":
                ones.append(i)

        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            candidate = s[start:end + 1]
        ans = ""

        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            candidate = s[start:end + 1]

            if ans == "" or len(candidate) < len(ans):
                ans = candidate

            elif len(candidate) == len(ans) and candidate < ans:
                ans = candidate
        return ans