from collections import Counter


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:

        n = len(s)

        # -----------------------------------------
        # 1. Frequency of characters
        # -----------------------------------------
        freq = Counter(s)

        # -----------------------------------------
        # 2. Check palindrome possibility
        # -----------------------------------------
        odd_count = 0
        middle = ""

        for ch, count in freq.items():

            if count % 2 != 0:
                odd_count += 1
                middle = ch

        if odd_count > 1:
            return ""

        # -----------------------------------------
        # 3. Frequency of characters in first half
        # -----------------------------------------
        half_count = Counter()

        for ch, count in freq.items():
            half_count[ch] = count // 2

        half_len = n // 2

        target_half = target[:half_len]

        # -----------------------------------------
        # 4. Find how many characters of target_half
        #    can exactly match our available chars
        # -----------------------------------------
        remaining = half_count.copy()

        equal_len = 0

        for i in range(half_len):

            ch = target_half[i]

            if remaining[ch] == 0:
                break

            remaining[ch] -= 1
            equal_len += 1

        # =================================================
        # 5. FIRST check:
        #
        # Can our first half be EXACTLY target_half?
        #
        # If yes, the resulting palindrome might already
        # be greater than target because of the middle/right
        # side.
        # =================================================

        if equal_len == half_len:

            candidate_half = target_half

            answer = (
                candidate_half
                + middle
                + candidate_half[::-1]
            )

            if answer > target:
                return answer

        # =================================================
        # 6. First half cannot itself give the answer.
        #
        # Now find the smallest first half that is
        # STRICTLY GREATER than target_half.
        #
        # We go RIGHT -> LEFT so that we change the
        # rightmost possible position.
        # =================================================

        start = min(equal_len, half_len - 1)

        for i in range(start, -1, -1):

            # Rebuild frequency
            remaining = half_count.copy()

            possible = True

            # -----------------------------------------
            # Keep everything before i equal to target
            # -----------------------------------------
            for j in range(i):

                ch = target_half[j]

                if remaining[ch] == 0:
                    possible = False
                    break

                remaining[ch] -= 1

            if not possible:
                continue

            # -----------------------------------------
            # At position i, choose smallest character
            # strictly greater than target_half[i]
            # -----------------------------------------
            target_ch = target_half[i]

            for ch in "abcdefghijklmnopqrstuvwxyz":

                if ch <= target_ch:
                    continue

                if remaining[ch] == 0:
                    continue

                # Use this character
                remaining[ch] -= 1

                candidate_half = target_half[:i] + ch

                # -----------------------------------------
                # Fill remaining positions with smallest
                # available characters
                # -----------------------------------------
                for c in "abcdefghijklmnopqrstuvwxyz":
                    candidate_half += c * remaining[c]

                # -----------------------------------------
                # Build palindrome
                # -----------------------------------------
                answer = (
                    candidate_half
                    + middle
                    + candidate_half[::-1]
                )

                if answer > target:
                    return answer

                # Undo
                remaining[ch] += 1

        return ""