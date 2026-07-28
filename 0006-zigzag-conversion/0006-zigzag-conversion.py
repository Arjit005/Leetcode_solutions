class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: no zigzag if only 1 row
        if numRows == 1 or len(s) <= numRows:
            return s
        
        # Zigzag cycle repeats every (2*numRows - 2) characters
        cycle = 2 * numRows - 2
        rows = ["" for _ in range(numRows)]
        
        for i, char in enumerate(s):
            pos_in_cycle = i % cycle
            
            # Down phase (0→1→2→...) vs Up phase (bounce back)
            if pos_in_cycle < numRows:
                row = pos_in_cycle
            else:
                row = cycle - pos_in_cycle
            
            rows[row] += char
        
        return ''.join(rows)