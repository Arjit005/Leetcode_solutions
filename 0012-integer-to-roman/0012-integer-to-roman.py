class Solution:
    def intToRoman(self, num: int) -> str:

        # symbols
        symbol = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        # We have to process the number
        # from largest place value to smallest place value.
        """
        number
           ↓
        find largest Roman value that fits
           ↓
        append its symbol
           ↓
        subtract its value
           ↓
        repeat
        """

        # We use the greedy algorithm because:
        # At every step, choose the largest Roman numeral
        # value that can fit into the remaining number.

        """
        1. Take the largest value that fits
        2. Add its Roman symbol
        3. Subtract that value from num
        4. Repeat
        """
        #A greedy algorithm means:

        # At each step, make the best/largest choice available right now, without reconsidering previous choices.

        roman = ""  # We use a string to build the answer

        # Take the largest value first
        for value in symbol:

            # Keep using the current value
            # as long as it fits in num.
            while num >= value:  #Try the largest possible value first.

                # Add the Roman symbol corresponding to the value
                roman += symbol[value]

                # Remove the value we just converted
                num -= value

        return roman