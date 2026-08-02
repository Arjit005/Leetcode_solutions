# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # pointer mainpulation makes it hard
        #These will became separate lists
        #After every reversal, the old first node becomes the last node. That node is called the tail of the reversed group.
        #The tail is where the next reversed group will later attach.

        # prob 1==> Who changes the head?  , create the dummy node head always point 

        #So we simply change  dummy.next  ,The dummy now points to the new head.

        # create dummy node
        dummy=ListNode(0)
        dummy.next=head

        group_prev=dummy


        while True:
            kth=group_prev

            for _ in range(k):
                if not kth.next:
                    return dummy.next
                kth=kth.next
            group_next=kth.next
            #Prepare for reversal
            prev=group_next
            curr=group_prev.next   
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            # Connect reversed group back
            temp = group_prev.next    # Old head of group (becomes tail)

            group_prev.next = kth     # Connect previous part to new head
            group_prev = temp         # Move group_prev to the new tail    