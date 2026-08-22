class Solution:
    def productExceptSelf(self, nums):
        zeros = 0
        prod = 1
        n = len(nums)

        # Count zeros and calculate product of non-zero numbers
        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            else:
                prod *= nums[i]

        res = [0] * n

        # More than one zero
        if zeros > 1:
            return res

        # No zero
        elif zeros == 0:
            res = []
            for i in range(n):
                res.append(prod // nums[i])
            return res

        # Exactly one zero
        else:
            zero_index = -1

            for i in range(n):
                if nums[i] == 0:
                    zero_index = i
                    break

            res[zero_index] = prod
            return res