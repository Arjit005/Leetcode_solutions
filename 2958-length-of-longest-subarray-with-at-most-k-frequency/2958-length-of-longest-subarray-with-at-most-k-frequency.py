from collections import Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        """
        GOAL
        ─────────────────────────────────────────────
        Find the LONGEST CONTINUOUS subarray
        where every number appears <= k times.


        MAIN IDEA
        ─────────────────────────────────────────────

                    WINDOW
        ┌──────────────────────────────┐
        │ [ left .............. right ]│
        └──────────────────────────────┘
           ↑                    ↑
         LEFT                 RIGHT

        RIGHT → expands the window
        LEFT  → shrinks the window
        """

        # freq = number of times that an element occurred
        # Every element's frequency must be <= k.

        """
        WHY EMPTY COUNTER?
        ─────────────────────────────────────────────

        Counter(nums)
             ↓
        ┌─────────────────┐
        │ WHOLE ARRAY     │
        │ 1, 2, 1, 3, 2   │
        └─────────────────┘

        But our problem is about a SUBARRAY,
        not the whole array.

        We therefore need:

        CURRENT WINDOW
             ↓
          Counter
             ↓
        frequencies ONLY inside the window

        So we start with an EMPTY Counter
        and manually add/remove elements.
        """

        counter = Counter()

        """
        CREATE WINDOW
        ─────────────────────────────────────────────

        left = beginning of the window

        right will move through the array.

        [ 1  2  1  3  2 ]
          ↑
         LEFT
        """

        left = 0
        max_len = 0

        """
        RIGHT EXPANDS
        ─────────────────────────────────────────────

        right →
             ↓
        [ 1  2  1  3  2 ]
          ↑        ↑
        LEFT     RIGHT

        Every time RIGHT moves,
        a new element enters the window.
        """

        for right in range(len(nums)):

            """
            ADD NEW ELEMENT
            ─────────────────────────────────────────

            New element enters the window
                         ↓
            [ ...  nums[right] ]
                         ↓
                    Counter + 1

            Counter now represents
            frequencies INSIDE the current window.
            """

            counter[nums[right]] += 1

            """
            CHECK WINDOW
            ─────────────────────────────────────────

                    COUNTER
                       ↓
            frequency of new element > k ?
                    /           \
                  YES           NO
                   ↓             ↓
              INVALID          VALID
                   ↓             ↓
                SHRINK         continue
            """

            while counter[nums[right]] > k:

                """
                SHRINK FROM LEFT
                ─────────────────────────────────────

                Current window:

                    LEFT
                      ↓
                [ 1  2  1  3  1 ]
                  ↑
                remove this element

                Because the window is continuous,
                the easiest way to make it smaller
                is to remove from the LEFT.
                """

                counter[nums[left]] -= 1

                """
                MOVE LEFT
                ─────────────────────────────────────

                Before:

                [ LEFT ............ RIGHT ]
                  ↑

                After:

                [   LEFT .......... RIGHT ]
                    ↑
                    →
                """

                left += 1

                """
                WHY WHILE?
                ─────────────────────────────────────

                Removing ONE element may NOT
                make the window valid.

                Example:

                k = 2

                [ 1  1  1  1 ]
                  frequency = 4  ❌

                remove one:

                [ 1  1  1 ]
                  frequency = 3  ❌

                remove again:

                [ 1  1 ]
                  frequency = 2  ✅

                Therefore:

                WHILE invalid
                    ↓
                keep shrinking
                    ↓
                until valid
                """

            """
            WINDOW IS VALID
            ─────────────────────────────────────────

            Now we know:

                  [ LEFT ........ RIGHT ]
                        VALID ✅

            Length of this window:

                right - left + 1

            Compare it with the best answer
            found so far.
            """

            max_len = max(max_len, right - left + 1)

        """
        FINAL ANSWER
        ─────────────────────────────────────────────

        max_len = longest valid window found
        """

        return max_len