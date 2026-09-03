# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            mylist = ListNode(head.val)
        else:
            return
        curr = head
        while curr.next:
            curr = curr.next
            mylist = ListNode(curr.val,mylist)
        return mylist
            