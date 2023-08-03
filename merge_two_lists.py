# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ptr1 = list1
        ptr2 = list2
        list3 = ListNode();
        head = list3
        while ptr1 != None and ptr2 != None:
            if ptr1.val < ptr2.val:
                list3.next = ptr1
                ptr1 = ptr1.next
            else:
                list3.next = ptr2
                ptr2 = ptr2.next 
            list3 = list3.next    

        list3.next = ptr2 if ptr1 == None else ptr1
        return head.next
