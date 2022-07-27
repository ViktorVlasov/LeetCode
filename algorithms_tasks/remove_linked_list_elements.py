#https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(val=None, next=head)

        cur = head
        prev = dummy

        while cur != None:
            if cur.val != val:
                prev = cur
            else:
                prev.next = cur.next
            cur = cur.next

        return dummy.next