from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        # ============================================================
        # LEVEL 0: What problem are we solving?
        # ============================================================
        #
        # 1. s ke characters ki permutation banani hai
        # 2. Jo permutation target se strictly greater ho
        # 3. Unmein se lexicographically smallest permutation return karni hai
        # 4. Agar koi valid permutation nahi hai -> ""
        #
        # Lexicographical order:
        # Pehli different position ka character decide karta hai
        # ki kaunsi string greater hai.
        #
        # Example:
        # "bca" > "bba"
        #
        # Kyunki:
        # b = b
        # c > b
        # ============================================================


        # ============================================================
        # LEVEL 1: Counter
        # ============================================================
        #
        # Humein s ke characters ki frequency pata honi chahiye.
        #
        # Example:
        # s = "aabc"
        #
        # count_freq:
        # a -> 2
        # b -> 1
        # c -> 1
        #
        # Counter hamara character inventory hai.
        # ============================================================

        count_freq = Counter(s)


        # ============================================================
        # LEVEL 2: Main idea
        # ============================================================
        #
        # Humein saare permutations generate nahi karne.
        #
        # Kyunki n <= 300 hai aur n! permutations ho sakti hain.
        #
        # Iske badle:
        #
        # Prefix       -> target jaisa rakho
        # Changed char -> target[i] se smallest greater character
        # Suffix       -> remaining characters smallest -> largest
        #
        # Hum RIGHT -> LEFT jayenge.
        #
        # Why?
        # Jitni right position par change karenge,
        # utna zyada target ka prefix same rahega.
        #
        # Isliye resulting string minimum possible greater string hogi.
        # ============================================================


        # ============================================================
        # LEVEL 3: Right -> Left
        # ============================================================
        #
        # Example:
        #
        # target = "bba"
        #
        # positions:
        #          0 1 2
        #          b b a
        #
        # Hum try karenge:
        #
        # right = 2
        # right = 1
        # right = 0
        #
        # Har position par check karenge:
        #
        # target[:right]
        #
        # kya s ke available characters se ban sakta hai?
        # ============================================================

        for right in range(len(target) - 1, -1, -1):


            # ========================================================
            # LEVEL 4: Fresh Counter
            # ========================================================
            #
            # Har position ke liye fresh Counter chahiye.
            #
            # Kyunki hum target ke prefix ko temporarily consume
            # kar rahe hain.
            #
            # Example:
            #
            # s = "aabc"
            #
            # count_freq:
            # a -> 2
            # b -> 1
            # c -> 1
            #
            # copy banane ke baad isi copy ko decrease karenge.
            # ========================================================

            remaining_count = count_freq.copy()

            possible = True


            # ========================================================
            # LEVEL 5: Target ka prefix consume karo
            # ========================================================
            #
            # target[:right] ka matlab:
            #
            # right = 2
            # target = "bba"
            #
            # target[:2] = "bb"
            #
            # Matlab sirf prefix consume hoga.
            # target[right] ko abhi consume nahi karenge,
            # kyunki isi character ko baad mein bigger character
            # se replace karne ki koshish karenge.
            # ========================================================

            for i in range(right):

                ch = target[i]

                # Agar character available hai,
                # toh uski frequency 1 decrease karo.
                if remaining_count[ch] > 0:

                    remaining_count[ch] -= 1

                else:
                    # Character available nahi hai.
                    #
                    # Matlab target ka ye prefix
                    # s ke characters se nahi ban sakta.
                    possible = False
                    break


            # ========================================================
            # Prefix hi nahi ban sakta
            # ========================================================
            #
            # Example:
            #
            # s = "abc"
            # target = "bba"
            #
            # right = 2
            #
            # target[:2] = "bb"
            #
            # s mein sirf ek 'b' hai.
            # Isliye "bb" nahi bana sakte.
            #
            # Ab next position par try karenge.
            # ========================================================

            if not possible:
                continue


            # ========================================================
            # LEVEL 6: Bigger character find karo
            # ========================================================
            #
            # Ab target[right] ko dekho.
            #
            # Humein aisa character chahiye:
            #
            # character > target[right]
            #
            # Aur humein SMALLest greater character chahiye.
            #
            # Example:
            #
            # target[right] = 'b'
            #
            # Available:
            # a, c, d
            #
            # c > b
            # d > b
            #
            # Lekin c smallest greater hai.
            # ========================================================

            current = target[right]
            bigger = None

            for code in range(ord(current) + 1, ord('z') + 1):

                ch = chr(code)

                if remaining_count[ch] > 0:

                    bigger = ch
                    break


            # ========================================================
            # Is position par greater character nahi mila
            # ========================================================
            #
            # Agar bigger None hai,
            # toh current position par answer possible nahi hai.
            #
            # Ab left wali position try karo.
            # ========================================================

            if bigger is None:
                continue


            # ========================================================
            # LEVEL 7: Bigger character consume karo
            # ========================================================
            #
            # Maan lo:
            #
            # target[right] = 'b'
            # bigger = 'c'
            #
            # Hum 'c' use kar rahe hain.
            #
            # Isliye:
            #
            # c -> c - 1
            # ========================================================

            remaining_count[bigger] -= 1


            # ========================================================
            # LEVEL 8: Prefix + bigger character
            # ========================================================
            #
            # target[:right]
            #       +
            # bigger
            #
            # Example:
            #
            # target = "bba"
            # right = 1
            # bigger = "c"
            #
            # target[:1] = "b"
            #
            # answer = "bc..."
            # ========================================================

            answer = target[:right] + bigger


            # ========================================================
            # LEVEL 9: Remaining characters
            # ========================================================
            #
            # Ab answer already target se greater hai.
            #
            # Isliye remaining characters ko:
            #
            # smallest -> largest
            #
            # order mein lagayenge.
            #
            # Kyunki humein lexicographically SMALLEST greater
            # permutation chahiye.
            # ========================================================

            for ch in sorted(remaining_count):

                answer += ch * remaining_count[ch]


            # ========================================================
            # Valid answer mil gaya
            # ========================================================

            return answer


        # ============================================================
        # Koi bhi permutation target se strictly greater nahi hai.
        # ============================================================

        return ""