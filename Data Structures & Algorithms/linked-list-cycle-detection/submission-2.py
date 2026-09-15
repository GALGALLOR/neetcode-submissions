# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mymap = {}
        index = 0
        while head:
            if mymap.get(head,0)>0:
                return True
            else:
                mymap[head] = 1
            head = head.next
        return False