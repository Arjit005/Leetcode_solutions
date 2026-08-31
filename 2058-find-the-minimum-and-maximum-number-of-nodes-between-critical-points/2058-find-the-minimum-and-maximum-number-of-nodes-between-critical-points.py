# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        # First and last node cannot be critical
        # So we need at least 3 nodes
        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        # prev -> previous node
        # curr -> current node
        prev = head
        curr = head.next

        position = 2

        first_critical = -1
        prev_critical = -1

        min_distance = float('inf')

        while curr and curr.next:

            is_maxima = (
                curr.val > prev.val and
                curr.val > curr.next.val
            )

            is_minima = (
                curr.val < prev.val and
                curr.val < curr.next.val
            )

            if is_maxima or is_minima:

                # First critical point
                if first_critical == -1:
                    first_critical = position

                # We already have a previous critical point
                if prev_critical != -1:
                    min_distance = min(
                        min_distance,
                        position - prev_critical
                    )

                # Current critical point becomes previous
                prev_critical = position

            prev = curr
            curr = curr.next
            position += 1

        # Fewer than two critical points
        if first_critical == -1 or prev_critical == first_critical:
            return [-1, -1]

        # Distance between first and last critical point
        max_distance = prev_critical - first_critical

        return [min_distance, max_distance]
