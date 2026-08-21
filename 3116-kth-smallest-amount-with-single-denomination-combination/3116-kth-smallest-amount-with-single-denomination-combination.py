from math import gcd
class Solution: 
    def findKthSmallest(self, coins: List[int], k: int) -> int: 
        """
        ================================================================
        STEP 0: UNDERSTAND THE PROBLEM
        ================================================================

        Imagine you are building stacks of coins.

        Rule:
        Each stack can contain only ONE type of coin.

        If you have a $2 coin:
            Using only $2 coins:
            2, 4, 6, 8, 10, 12, 14...

        If you have a $5 coin:
            Using only $5 coins:
            5, 10, 15, 20...

        Now combine all possible amounts, sort them, and remove
        duplicates.

        Example:

            2, 4, 5, 6, 8, 10, 12, 14, 15...

        The problem asks:

            "What is the k-th number in this sequence?"

        Example:
            If k = 7

            1 -> 2
            2 -> 4
            3 -> 5
            4 -> 6
            5 -> 8
            6 -> 10
            7 -> 12

            Answer = 12


        ================================================================
        STEP 1: READ THE CONSTRAINTS LIKE CLUES
        ================================================================

        There are two extremely important constraints:

            1. k <= 2 * 10^9
            2. len(coins) <= 15


        -------------------------
        CLUE 1: k IS HUGE
        -------------------------

        k can be as large as 2 billion.

        Therefore, we cannot generate the sequence one number at
        a time until we reach the k-th number.

        For example:

            for x in range(...):
                ...

        Trying to generate billions of numbers would be far too slow.

        A Min-Heap would also be problematic because we might need to
        generate a huge number of elements before reaching the answer.

        Therefore:

            We need a way to JUMP toward the answer.

        This points toward:

            Binary Search


        -------------------------
        CLUE 2: coins.length <= 15
        -------------------------

        Why is the number of coins so small?

        Because we will need to examine combinations/subsets of coins.

        If there are n coins:

            Number of subsets = 2^n

        For n = 15:

            2^15 = 32,768

        That is small enough to process.

        Therefore:

            Small number of coins
                    ↓
            Try every subset
                    ↓
            Inclusion-Exclusion


        ================================================================
        STEP 2: THE BIG IDEA — DON'T BUILD THE SEQUENCE
        ================================================================

        The sequence might contain billions of possible values.

        Instead of actually building it, we ask a different question:

            "How many valid amounts are <= x?"

        This changes the problem from:

            "Find the k-th number."

        into:

            "For a given x, how many valid numbers are <= x?"


        This is the key idea behind:

            Binary Search on Answer


        ================================================================
        STEP 3: BINARY SEARCH ON THE ANSWER
        ================================================================

        Imagine you want to find the 5th highest score in a huge
        video-game tournament.

        The naive way:

            Look at every player's score.
            Sort everybody.
            Pick the 5th highest.

        That is similar to generating our entire sequence.


        Instead, guess a score:

            "Suppose the answer is 8,500."

        Then ask:

            "How many players scored >= 8,500?"


        If there are too many players:

            8,500 is too LOW.

            Move toward a higher score.


        If there are too few players:

            8,500 is too HIGH.

            Move toward a lower score.


        We repeatedly narrow the search range.

        That is Binary Search.


        ================================================================
        STEP 4: WHAT DOES BINARY SEARCH NEED?
        ================================================================

        Binary Search needs a function that can answer:

            count(x)

        Meaning:

            "How many valid amounts are <= x?"


        Example:

            coins = [2, 5]
            x = 10

        Multiples of 2 <= 10:

            2, 4, 6, 8, 10
            -> 5 numbers

        Multiples of 5 <= 10:

            5, 10
            -> 2 numbers


        We might initially think:

            5 + 2 = 7


        But this is WRONG.


        Why?

        Because 10 belongs to BOTH groups.

            Multiples of 2:  2, 4, 6, 8, 10
            Multiples of 5:  5, 10

        We counted 10 twice.


        Therefore:

            We need Inclusion-Exclusion.


        ================================================================
        STEP 5: INCLUSION-EXCLUSION
        ================================================================

        Inclusion-Exclusion means:

            INCLUDE groups
            EXCLUDE overlaps
            INCLUDE overlaps of 3 groups
            EXCLUDE overlaps of 4 groups
            ...

        The pattern is:

            1 coin  -> ADD
            2 coins -> SUBTRACT
            3 coins -> ADD
            4 coins -> SUBTRACT
            5 coins -> ADD
            ...


        In other words:

            Odd number of selected coins
                -> ADD

            Even number of selected coins
                -> SUBTRACT


        Why?

        Because every time we combine another group, we are correcting
        the over-counting created by the previous step.


        Example with coins [2, 5]:

            Multiples of 2 <= 10 = 5
            Multiples of 5 <= 10 = 2

            Add:
                5 + 2 = 7

            Both 2 and 5 divide 10.

            Their common multiples are multiples of:

                LCM(2, 5) = 10

            Common multiples <= 10:

                10

            Subtract the overlap:

                7 - 1 = 6


        The six valid numbers are:

            2, 4, 5, 6, 8, 10


        ================================================================
        STEP 6: BUT HOW DO WE CHECK EVERY SUBSET?
        ================================================================

        We have at most 15 coins.

        Therefore, we can examine every subset.

        For example:

            coins = [2, 3, 5]

        Possible subsets:

            {}
            {2}
            {3}
            {5}
            {2,3}
            {2,5}
            {3,5}
            {2,3,5}

        Total:

            2^3 = 8 subsets


        For 15 coins:

            2^15 = 32,768 subsets

        This is manageable.


        ================================================================
        STEP 7: BITMASKING
        ================================================================

        Instead of creating an actual list for every subset, we can
        represent a subset using BITS.

        Example:

            coins = [2, 3, 5]

        Think of each bit as a switch:

            bit 0 -> coin 2
            bit 1 -> coin 3
            bit 2 -> coin 5


        A bit of:

            1 = coin is selected
            0 = coin is NOT selected


        Example:

            001

        Means:

            coin 2 -> selected
            coin 3 -> not selected
            coin 5 -> not selected

        Therefore:

            {2}


        Another example:

            101

        Means:

            coin 2 -> selected
            coin 3 -> not selected
            coin 5 -> selected

        Therefore:

            {2, 5}


        And:

            111

        Means:

            {2, 3, 5}


        We can therefore use integers:

            1
            2
            3
            ...
            2^n - 1

        to represent all non-empty subsets.


        ================================================================
        STEP 8: WHY BITMASKING FITS THIS PROBLEM
        ================================================================

        The important point is not that bitmasks magically make the
        algorithm free.

        The important point is:

            We need to enumerate subsets.

        Bitmasking gives us a compact way to represent each subset
        without creating a separate list for every subset.

        For n = 15:

            Number of masks = 2^15 - 1
                           = 32,767

        Each mask tells us exactly which coins are selected.


        ================================================================
        STEP 9: BITMASK -> NUMBER OF SELECTED COINS
        ================================================================

        Remember Inclusion-Exclusion:

            1 selected coin  -> ADD
            2 selected coins -> SUBTRACT
            3 selected coins -> ADD
            4 selected coins -> SUBTRACT


        So we need to know:

            "How many coins are selected in this mask?"


        This is called:

            POPCOUNT

        Example:

            mask = 101

        Number of 1s:

            2

        Therefore:

            2 selected coins
            -> EVEN
            -> SUBTRACT


        Example:

            mask = 111

        Number of 1s:

            3

        Therefore:

            3 selected coins
            -> ODD
            -> ADD


        ================================================================
        STEP 10: THE COMPLETE MENTAL PICTURE
        ================================================================

        The whole solution can now be viewed as a chain:

            We need the k-th smallest valid number
                            ↓
            k can be 2 billion
                            ↓
            Cannot generate the sequence
                            ↓
            Binary Search on the answer
                            ↓
            Binary Search needs count(x)
                            ↓
            count(x) = number of valid amounts <= x
                            ↓
            Multiple coins create overlapping multiples
                            ↓
            Need Inclusion-Exclusion
                            ↓
            coins.length <= 15
                            ↓
            We can examine every subset
                            ↓
            Use Bitmasking to represent subsets
                            ↓
            Odd number of selected coins -> ADD
            Even number of selected coins -> SUBTRACT


        ================================================================
        IMPORTANT MEMORY HOOK
        ================================================================

        Don't memorize the final algorithm as one giant formula.

        Remember these questions:

            1. Why can't I generate the sequence?
                   -> k is huge

            2. How can I find the answer without generating it?
                   -> Binary Search

            3. What does Binary Search need?
                   -> count(x)

            4. How do I count numbers produced by multiple coins?
                   -> Inclusion-Exclusion

            5. How do I check all combinations?
                   -> Bitmasking

            6. How do I know ADD or SUBTRACT?
                   -> Number of selected coins
                      Odd  -> ADD
                      Even -> SUBTRACT
        """
        #The complete chain

        # k-th smallest→Binary Search→count(x)→Inclusion–Exclusion→Subsets→Bitmask


        #Super-Fast Counter (Bitmasking + Inclusion-Exclusion).
        # ---------------------------------------------------------------
        # The actual solution starts here.
        #
        # First goal:
        # Build the function that answers:
        #
        #     "How many valid numbers are <= x?"
        #
        # Don't try to write Binary Search immediately.
        # Solve the counting problem first.
        # ---------------------------------------------------------------

        # overlap == LCM  ---> a*b/gcd(a,b)

        def count(x):
            counts = 0

            for mask in range(1, 1 << len(coins)):

                lcm = 1
                selected = 0

                for i in range(len(coins)):
                    if mask & (1 << i):

                        selected += 1

                        lcm = lcm * coins[i] // gcd(lcm, coins[i])

                if selected % 2 == 1:
                    counts += x // lcm
                else:
                    counts -= x // lcm

            return counts


        """
        bisect
        ↓
        search inside an existing sorted array


        Our Binary Search
        ↓
        search the possible ANSWER range
        ↓
        [low .............. high]
        ↓
        use count(mid) to decide which half to keep
        """    
        low = min(coins)
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low