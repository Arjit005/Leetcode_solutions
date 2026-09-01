from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m = len(classroom)
        n = len(classroom[0])

        # Find start and assign an index to every litter
        start = None
        litter = {}

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)

                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        total_litter = len(litter)

        # No litter to collect
        if total_litter == 0:
            return 0

        full_mask = (1 << total_litter) - 1

        # visited[r][c][mask] = maximum energy with which
        # we have reached (r,c) having collected mask.
        visited = [
            [
                [-1] * (1 << total_litter)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        sr, sc = start

        queue = deque()

        # row, col, remaining_energy, mask, moves
        queue.append((sr, sc, energy, 0, 0))

        visited[sr][sc][0] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:

            r, c, curr_energy, mask, moves = queue.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Outside grid
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Cannot move if energy is already 0
                if curr_energy == 0:
                    continue

                # Moving costs 1 energy
                new_energy = curr_energy - 1

                new_mask = mask

                # Collect litter if present
                if classroom[nr][nc] == 'L':
                    litter_id = litter[(nr, nc)]
                    new_mask |= (1 << litter_id)

                # Reset energy when entering R
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # Did we collect everything?
                if new_mask == full_mask:
                    return moves + 1

                # If we have already reached this
                # (position, mask) with >= energy,
                # this state is useless.
                if visited[nr][nc][new_mask] >= new_energy:
                    continue

                visited[nr][nc][new_mask] = new_energy

                queue.append(
                    (
                        nr,
                        nc,
                        new_energy,
                        new_mask,
                        moves + 1
                    )
                )

        return -1