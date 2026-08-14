from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        # substring ==> continuous sequence of characters

        """
        | Problem type                          | Main technique                     |
        |---------------------------------------|-------------------------------------|
        | Fixed length substring                | Sliding Window                     |
        | Longest/shortest satisfying condition | Variable Sliding Window            |
        | Character frequency condition         | Counter + Window                   |
        | Palindromic substring                 | Expand Around Center               |
        | All possible substrings               | Nested loops / optimized technique |
        """

        """
                     SUBSTRING
                        │
                        ▼
                Is length fixed?
                /          \
              YES           NO
               │             │
               ▼             ▼
        Fixed Window     Is there a condition?
                            /      \
                          YES       NO
                           │         │
                           ▼         ▼
                   Sliding Window   Other
                           │
                           ▼
                    What condition?
                    /     |       \
              frequency  unique   sum/etc.
                  │         │        │
                  ▼         ▼        ▼
               Counter     Set     variable
        """

        # That means our current window is valid when:
        # every character's frequency <= 2

        count = Counter()  # currently Counter is empty

        # So our Counter will track the frequency
        # inside the current window.

        left = 0

        # We will use ans to calculate the maximum length
        ans = 0

        for right in range(len(s)):

            # Add new character into Counter
            count[s[right]] += 1

            # If any character occurs more than 2 times,
            # shrink the window from the left
            while count[s[right]] > 2:

                # Give me the value (frequency) associated
                # with the key s[left].
                count[s[left]] -= 1

                # Move the left pointer forward
                left = left + 1

            # Current window is valid.
            # Window = s[left : right + 1]
            # Its length = right - left + 1
            ans = max(ans, right - left + 1)

        return ans
