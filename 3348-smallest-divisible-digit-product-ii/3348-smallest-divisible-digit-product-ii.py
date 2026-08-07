class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t into factors of 2, 3, 5, 7
        count = {2: 0, 3: 0, 5: 0, 7: 0}
        temp_t = t
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                count[p] += 1
                temp_t //= p
        if temp_t > 1:
            return "-1"  # Contains prime factor > 7 (e.g., 11, 13)

        need2, need3, need5, need7 = count[2], count[3], count[5], count[7]

        # Helper: Minimum digits needed to satisfy remaining prime factor counts
        def get_min_digits(c2, c3, c5, c7):
            # Combine factors into largest single-digit multipliers
            d9 = c3 // 2
            c3 %= 2

            d8 = c2 // 3
            c2 %= 3

            d7 = c7
            d5 = c5

            d6 = 0
            if c2 > 0 and c3 > 0:
                d6 = 1
                c2 -= 1
                c3 -= 1

            d4 = c2 // 2
            c2 %= 2

            d3 = c3
            d2 = c2

            digits = []
            digits.extend(['2'] * d2)
            digits.extend(['3'] * d3)
            digits.extend(['4'] * d4)
            digits.extend(['5'] * d5)
            digits.extend(['6'] * d6)
            digits.extend(['7'] * d7)
            digits.extend(['8'] * d8)
            digits.extend(['9'] * d9)
            digits.sort()
            return digits

        # Helper: Construct smallest suffix of target length given needed factors
        def make_suffix(c2, c3, c5, c7, length):
            req_digits = get_min_digits(c2, c3, c5, c7)
            if len(req_digits) > length:
                return None
            # Pad with '1's on the left to reach exact length
            ones_needed = length - len(req_digits)
            return "".join(['1'] * ones_needed + req_digits)

        # Helper: Returns (c2, c3, c5, c7) contribution of a single digit
        def get_factors(d):
            if d == 0:
                return None
            f = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in [2, 3, 5, 7]:
                while d % p == 0:
                    f[p] += 1
                    d //= p
            return f[2], f[3], f[5], f[7]

        n = len(num)

        # Check if the original num itself works (if it has no zeros)
        if '0' not in num:
            c2 = c3 = c5 = c7 = 0
            for ch in num:
                f2, f3, f5, f7 = get_factors(int(ch))
                c2 += f2
                c3 += f3
                c5 += f5
                c7 += f7
            if c2 >= need2 and c3 >= need3 and c5 >= need5 and c7 >= need7:
                return num

        # Try to match a prefix of length i, then pick a larger digit at position i
        # Find prefix factor counts
        pref_factors = [(0, 0, 0, 0)] * (n + 1)
        valid_prefix = True
        for i in range(n):
            if num[i] == '0':
                valid_prefix = False
                break
            f2, f3, f5, f7 = get_factors(int(num[i]))
            p2, p3, p5, p7 = pref_factors[i]
            pref_factors[i + 1] = (p2 + f2, p3 + f3, p5 + f5, p7 + f7)

        # Iterate right-to-left for the position of first mismatch/increase
        for i in range(n - 1, -1, -1):
            if not valid_prefix and i > num.find('0'):
                continue  # Cannot reuse prefix that contains '0'

            p2, p3, p5, p7 = pref_factors[i]
            old_digit = int(num[i])

            for new_digit in range(old_digit + 1, 10):
                f2, f3, f5, f7 = get_factors(new_digit)
                rem2 = max(0, need2 - (p2 + f2))
                rem3 = max(0, need3 - (p3 + f3))
                rem5 = max(0, need5 - (p5 + f5))
                rem7 = max(0, need7 - (p7 + f7))

                suf = make_suffix(rem2, rem3, rem5, rem7, n - 1 - i)
                if suf is not None:
                    return num[:i] + str(new_digit) + suf

        # If no valid number of length n exists, create a number of length n + k
        req_digits = get_min_digits(need2, need3, need5, need7)
        target_len = max(n + 1, len(req_digits))
        ones_needed = target_len - len(req_digits)
        return "".join(['1'] * ones_needed + req_digits)