class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):

        n = len(s)

        # tree[node] stores:
        #
        # [left_char, right_char,
        #  length, prefix, suffix, best]
        #
        # left_char  = first character in this segment
        # right_char = last character in this segment
        # length     = length of the segment
        # prefix     = longest same-character run from the left
        # suffix     = longest same-character run from the right
        # best       = longest same-character run anywhere
        tree = [None] * (4 * n)

        # ---------------------------------------------------------
        # MERGE TWO CHILDREN
        # ---------------------------------------------------------
        def merge(a, b):

            # The combined segment starts where a starts
            left_char = a[0]

            # The combined segment ends where b ends
            right_char = b[1]

            # Total length
            length = a[2] + b[2]

            # -----------------------------------------------------
            # PREFIX
            # -----------------------------------------------------

            # Normally the prefix comes completely from a
            prefix = a[3]

            # But if ALL of a is the same character
            # and that character matches b's first character,
            # then the prefix can continue into b.
            if a[3] == a[2] and a[1] == b[0]:
                prefix = a[2] + b[3]

            # -----------------------------------------------------
            # SUFFIX
            # -----------------------------------------------------

            # Normally the suffix comes completely from b
            suffix = b[4]

            # If ALL of b is the same character
            # and that character matches a's last character,
            # then the suffix can continue into a.
            if b[4] == b[2] and a[1] == b[0]:
                suffix = b[2] + a[4]

            # -----------------------------------------------------
            # BEST
            # -----------------------------------------------------

            # The answer can be:
            #
            # 1. completely inside a
            # 2. completely inside b
            # 3. crossing the boundary between a and b
            best = max(a[5], b[5])

            # If the boundary characters are equal,
            # the suffix of a joins the prefix of b.
            if a[1] == b[0]:
                crossing = a[4] + b[3]
                best = max(best, crossing)

            return [
                left_char,
                right_char,
                length,
                prefix,
                suffix,
                best
            ]

        # ---------------------------------------------------------
        # BUILD SEGMENT TREE
        # ---------------------------------------------------------
        def build(node, left, right):

            # Leaf node = one character
            if left == right:

                tree[node] = [
                    s[left],   # left_char
                    s[left],   # right_char
                    1,         # length
                    1,         # prefix
                    1,         # suffix
                    1          # best
                ]

                return

            mid = (left + right) // 2

            # Build left child
            build(
                node * 2,
                left,
                mid
            )

            # Build right child
            build(
                node * 2 + 1,
                mid + 1,
                right
            )

            # Combine children
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # ---------------------------------------------------------
        # UPDATE ONE CHARACTER
        # ---------------------------------------------------------
        def update(node, left, right, index, char):

            # We reached the character that must be changed
            if left == right:

                tree[node] = [
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                ]

                return

            mid = (left + right) // 2

            # Find which half contains index
            if index <= mid:

                update(
                    node * 2,
                    left,
                    mid,
                    index,
                    char
                )

            else:

                update(
                    node * 2 + 1,
                    mid + 1,
                    right,
                    index,
                    char
                )

            # The child changed.
            # Therefore this parent must be recalculated.
            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # Build the tree once
        build(1, 0, n - 1)

        answer = []

        # ---------------------------------------------------------
        # PROCESS EACH QUERY
        # ---------------------------------------------------------
        for char, index in zip(
            queryCharacters,
            queryIndices
        ):

            # Change s[index] -> char
            update(
                1,
                0,
                n - 1,
                index,
                char
            )

            # tree[1] represents the entire string.
            #
            # tree[1][5] = best run in the whole string.
            answer.append(tree[1][5])

        return answer
        