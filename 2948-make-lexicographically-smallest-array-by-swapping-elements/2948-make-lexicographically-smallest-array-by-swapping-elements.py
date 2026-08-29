class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # type hinting se itna samajh aa rha hai ki output list of integers hai
        # lexicographically smallest array by swapping elements
        # loops chalana possible nhhi lagta kyo ki billions times chalana padega 
        # we can choose any 2  indices and swap if nums[i]-nums[j]<=limit 
        # lexicographically smallest array that can be obtained by perfarming operation any number of time


        # problem ==> how many time we can use swapping -
        #limit batata hai:

        # Do values ke beech maximum allowed difference kitna ho sakta hai for ONE direct swap.
        # |nums[i] - nums[j]| <= limit

        # Aur operation any number of times kiya ja sakta hai.

        # aur ek problem ye hai ki kisko kisse swap krna hai ?
        # aur isi swapping may aisa array bnanana hia jo ki smallest ho 


        """

        Humein basically 3 kaam karne hain:

            1. values ko sort karo
                    ↓
            2. limit ke basis par groups banao
                    ↓
            3. har group ki values ko
            uske original indices par sorted order mein daalo

        """
        n = len(nums)

        arr = [(nums[i], i) for i in range(n)]
        arr.sort()

        ans = nums[:]

        i = 0

        while i < n:

            j = i

            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            indices = [arr[k][1] for k in range(i, j + 1)]
            indices.sort()

            for k, index in enumerate(indices):
                ans[index] = arr[i + k][0]

            i = j + 1

        return ans




    
        