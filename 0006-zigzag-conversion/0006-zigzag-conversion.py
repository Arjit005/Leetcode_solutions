class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: no zigzag pattern exists
        if numRows == 1 or len(s) <= numRows:
            return s
        
        # Zigzag pattern repeats every (2*numRows - 2) characters
        # For numRows=3: cycle=4 (down 3 rows, up 1 row = 4 total)
        cycle = 2 * numRows - 2
        rows = ["" for _ in range(numRows)]
        
        # Traverse string and place each character in correct row
        for i, char in enumerate(s):
            # Find position within current cycle (resets every 'cycle' characters)
            pos_in_cycle = i % cycle
            
            # Determine which row based on phase
            if pos_in_cycle < numRows:
                # Down phase: row increases 0→1→2
                row = pos_in_cycle
            else:
                # Up phase: row decreases (bounces back)
                row = cycle - pos_in_cycle
            
            # Add character to appropriate row
            rows[row] += char
        
        # Read all rows line by line
        return ''.join(rows)