# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Edge case: no linked lists
        if not lists:
            return None

        # Keep merging until only one list remains
        while len(lists) > 1:

            # Store merged lists of this round
            merged = []

            # Merge neighboring pairs
            # Example:
            # [L1,L2,L3,L4,L5]
            # -> merge(L1,L2)
            # -> merge(L3,L4)
            # -> merge(L5,None)
            for i in range(0, len(lists), 2):

                # First list of the pair
                l1 = lists[i]

                # Second list if it exists
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                # Merge the two sorted lists
                merged.append(self.merge(l1, l2))

            # Update lists for the next round
            lists = merged

        # Only one merged list remains
        return lists[0]

    def merge(self, l1, l2):

        # Dummy node makes building the answer easier
        dummy = ListNode(0)

        # Tail always points to the last node
        # of the merged list
        tail = dummy

        # Compare both lists until one becomes empty
        while l1 and l2:

            # Take the smaller node
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            # Move tail to the newly added node
            tail = tail.next

        # Attach whichever list is still remaining
        if l1:
            tail.next = l1
        else:
            tail.next = l2

        # Skip dummy node and return merged list
        return dummy.next