# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Base cases
        if list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        elif not list1 and not list2:
            return None
        else:
            pass
        
        ##since we have 2 occupied lists, let's take out the lesser one
        if list1.val < list2.val:
            mergeList = ListNode(list1.val)
            list1 = list1.next
        else:
            mergeList = ListNode(list2.val)
            list2 = list2.next
        nextList = mergeList

        while list1 or list2:
            #Base case incase one list is empty
            if not list1:
                mergeList.next = list2
                list2 = list2.next
                break
            if not list2:
                mergeList.next = list1
                list1 = list1.next
                break
            #check head of list1 and list2 against one another
            if list1.val < list2.val:
                mergeList.next = ListNode(list1.val)
                mergeList = mergeList.next
                list1 = list1.next
            else:
                mergeList.next = ListNode(list2.val)
                mergeList = mergeList.next
                list2 = list2.next 

        
        return nextList
        