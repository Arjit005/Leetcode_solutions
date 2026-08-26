class Solution:
    def countAndSay(self, n: int) -> str:

        current = "1"

        for _ in range(n - 1):

            result = []
            i = 0

            while i < len(current):

                j = i

                while j < len(current) and current[j] == current[i]:
                    j += 1

                count = j - i
                digit = current[i]

                result.append(str(count) + digit)

                i = j

            current = "".join(result)

        return current
