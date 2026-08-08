class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        #concepts==>
        """
        1️⃣ Subsequence — start here
                word1 = "xbcyz"
                word2 = "abc"

                select [0,1,2]

                word1[0] = x
                word1[1] = b
                word1[2] = c

                result = "xbc"

                word2  = "abc"

                        x b c
                        a b c
                        ↑
                        1 mismatch

                VALID ✅
        
        word1 → select indices → resulting string
                              ↓
                          compare with word2
                              ↓
                      mismatches <= 1 ?   
        2️⃣ Next concept: Hamming Distance

                Now we add the "almost equal" part.

                For two strings of the same length, Hamming distance means:

                How many positions contain different characters?      
            String A:    A  B  X  D  E
                        ↓  ↓  ↓  ↓  ↓
            String B:    A  B  C  D  Y   
            
            Now compare position by position:
            Position:    0  1  2  3  4
                        ↓  ↓  ↓  ↓  ↓
A:                      A  B  X  D  E
B:                      A  B  C  D  Y
                        │  │  ✗  │  ✗
                        │  │     │
                        │  │     └── different
                        │  └──────── same
                        └─────────── same

            here are 2 different positions:

                    X ≠ C
                    E ≠ Y

                    Therefore:

            Hamming Distance = 2

        """

        """
        WORD1
        index:    0   1   2   3   4
                    v   b   c   c   a
                    │
                    │
                    ▼
                Need 'a'
                    │
                    │
                    ▼
                Try smallest
                    index 0
                    │
                    ▼
                v → a
                    │
                    ▼
                1 change
                    │
                    ▼
                Can remaining "bc"
                be formed after 0?
                    │
                    YES
                    │
                    ▼
                TAKE 0
                    │
                    ▼
                [0, _, _]
                    │
                    │
                    ▼
                Need 'b'
                    │
                    ▼
                smallest index
                after 0 = 1
                    │
                    ▼
                b = b ✅
                    │
                    ▼
                TAKE 1
                    │
                    ▼
                [0, 1, _]
                    │
                    ▼
                Need 'c'
                    │
                    ▼
                smallest index
                after 1 = 2
                    │
                    ▼
                c = c ✅
                    │
                    ▼
                TAKE 2
                    │
                    ▼
                [0, 1, 2] ✅
                    
        What exactly is "greedy" here?

        It's this one decision rule:
                    CURRENT POSITION
                        ↓
                ┌─────────────────┐
                │ Try indices     │
                │ from smallest   │
                │ to largest      │
                └────────┬────────┘
                        ↓
                    Can this index
                    lead to a valid
                    full answer?
                    ↙       ↘
                YES        NO
                ↓          ↓
                TAKE       SKIP
                ↓          ↓
            move right   try next

        Prefix matching==>              
                            PREFIX MATCHING
                                │
                                ▼
                            word1 =  x   a   b   x   c
                                    0   1   2   3   4
                                    │
                                    │  scan LEFT → RIGHT
                                    ▼
                            word2 =  a   b   c
                                    ↑
                                    j = 0
                                    │
                                    │
                            ┌───────┴──────────────────────────────┐
                            │                                      │
                            ▼                                      │
                        i=0:  x ≠ a ❌                             │
                            don't move j                           │
                            prefix[0] = 0                          │
                            │                                      │
                            ▼                                      │
                        i=1:  a = a ✅                             │
                            move j → 1                             │
                            prefix[1] = 1                          │
                            │                                      │
                            ▼                                      │
                        i=2:  b = b ✅                             │
                            move j → 2                             │
                            prefix[2] = 2                          │
                            │                                      │
                            ▼                                      │
                        i=3:  x ≠ c ❌                             │
                            don't move j                           │
                            prefix[3] = 2                          │
                            │                                      │
                            ▼                                      │
                        i=4:  c = c ✅                             │
                            move j → 3                             │
                            prefix[4] = 3                          │
                            │                                      │
                            └────────────────────────────────────────┘


                        FINAL RESULT:

                        word1:     x     a     b     x     c
                        index:     0     1     2     3     4
                                │     │     │     │     │
                                ▼     ▼     ▼     ▼     ▼
                        prefix:    0     1     2     2     3


                        Meaning:

                        prefix[0] = 0  → matched ""
                        prefix[1] = 1  → matched "a"
                        prefix[2] = 2  → matched "ab"
                        prefix[3] = 2  → matched "ab"
                        prefix[4] = 3  → matched "abc"  

        5️⃣ Suffix Matching
                            SUFFIX MATCHING
                                │
                                ▼

                word1 =    x    a    b    x    c
                            0    1    2    3    4
                                        ↑
                                    start here
                                    RIGHT → LEFT
                                        │
                                        ▼

                    word2 =    a    b    c
                                    ↑
                                    need c

                            x    a    b    x    c
                                        ↑
                                    c = c ✅
                                        │
                                        ▼

                            word2 =    a    b    c
                                ↑
                                    need b

                            x    a    b    x    c
                                    ↑
                                b = b ✅
                                    │
                                    ▼

                    word2 =    a    b    c
                        ↑
                        need a

                            x    a    b    x    c
                                ↑
                                a = a ✅
                                │
                                ▼

                            "abc" matched from RIGHT

        PREFIX                         SUFFIX

        LEFT → RIGHT                   RIGHT → LEFT

        word2: A B C D E               word2: A B C D E
                ↑                               ↑
            start                            end


        And THAT is why we need both for the greedy solution:

                    CHOOSE INDEX i
                        │
                ┌───────────┴───────────┐
                ▼                       ▼
            BEFORE i                 AFTER i
                │                       │
            PREFIX                   SUFFIX
                │                       │
                └───────────┬───────────┘
                            ▼
                    Can the whole answer
                        still work?

        """

        """
                    word2
                ┌──────────┼──────────┐
                ↓          ↓          ↓
            BEFORE     CURRENT     AFTER
                │          │          │
                ▼          ▼          ▼
            PREFIX     mismatch    SUFFIX
                │          │          │
                └──────────┼──────────┘
                        ↓
                    Can everything
                        fit?
                        ↓
                        YES
                        ↓
                        TAKE i
        """

        """
        final

                SUBSEQUENCE
                    ↓
                Choose increasing indices
                    ↓
                HAMMING DISTANCE
                    ↓
                At most 1 mismatch
                    ↓
                GREEDY
                    ↓
                Choose smallest possible index
                    ↓
                But first ask:
                "Can the rest still work?"
                    ↓
                PREFIX + SUFFIX
                    ↓
                Check LEFT + CURRENT + RIGHT
                    ↓
                YES → take index
                NO  → try next index


                    INPUT
                    │
                ┌────────┴────────┐
                │                 │
                ▼                 ▼
            word1              word2
                │                 │
                └────────┬────────┘
                        ▼
                    PREPROCESS ONCE
                        │
                ┌───────────┴───────────┐
                ▼                       ▼
            LEFT → RIGHT            RIGHT → LEFT
                │                       │
                ▼                       ▼
            prefix[]                 suffix[]
                │                       │
                └───────────┬───────────┘
                            ▼
                        GREEDY
                        │
                        ▼
                    Try smallest index
                        │
                        ▼
                    Can it complete?
                        ↙         ↘
                    YES          NO
                    ↓            ↓
                    TAKE         SKIP
                    │            │
                    └─────┬──────┘
                        ▼
                    next position
                        │
                        ▼
                        repeat
                        │
                        ▼
                    FINAL ANSWER
        """

        n = len(word1)
        m = len(word2)

        # ---------------------------------------------------------
        # PREFIX
        # ---------------------------------------------------------

        prefix = [0] * n

        j = 0

        for i in range(n):
            if j < m and word1[i] == word2[j]:
                j += 1

            prefix[i] = j

        # ---------------------------------------------------------
        # SUFFIX
        # ---------------------------------------------------------

        suffix = [m] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):

            if j >= 0 and word1[i] == word2[j]:
                j -= 1

            suffix[i] = j + 1

        # ---------------------------------------------------------
        # GREEDY
        # ---------------------------------------------------------

        answer = []

        j = 0
        used_mismatch = False

        for i in range(n):

            # We have already matched all of word2.
            if j == m:
                break

            # Case 1: characters already match.
            if word1[i] == word2[j]:

                answer.append(i)
                j += 1

            # Case 2: use our one allowed mismatch.
            elif not used_mismatch:

                # word1[i] is used as the mismatching character.
                # Therefore, the remaining part must start from i + 1.
                if suffix[i + 1] <= j + 1:

                    answer.append(i)
                    j += 1
                    used_mismatch = True

        # ---------------------------------------------------------
        # FINAL CHECK
        # ---------------------------------------------------------

        if len(answer) == m:
            return answer

        return []