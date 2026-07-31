class Solution:
    def minimumPushes(self, word: str) -> int:
        # create array frequency
        frequency=[0]*26
        for ch in word:
            frequency[ord(ch)-ord('a')]+=1
        # sort freq in reverse order
        frequency.sort(reverse=True)

        Total_cost=0
        for i in range(26):
            if frequency[i]==0:
                break
            # calculate push count
            push_count=i//8+1
            Total_cost+=frequency[i]*push_count
        return Total_cost