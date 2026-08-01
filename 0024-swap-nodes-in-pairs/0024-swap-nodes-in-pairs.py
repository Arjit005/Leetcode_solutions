# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy node before linked list
        dummy=ListNode(0)
        dummy.next=head

        # node before current pair
        prev=dummy

        # we will  continue at least two nodes remain
        while prev.next and prev.next.next:
            # current pair
            first=prev.next
            second=first.next

            # swap
            first.next=second.next
            second.next=first
            prev.next=second

            # move to next pair
            prev=first
        return dummy.next