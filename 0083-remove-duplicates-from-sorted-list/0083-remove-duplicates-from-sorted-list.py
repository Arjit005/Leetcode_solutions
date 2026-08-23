# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #To remove duplicates, we don't need a hash set or temporary buffer to remember values we've seen. We only need to look at the current node and its immediate neighbor. If they have the same value, the neighbor is a duplicate and can be removed.
        curr=head
        while  curr and  curr.next :
            if curr.val==curr.next.val:
                curr.next = curr.next.next
            else:
                curr=curr.next
        return head
         