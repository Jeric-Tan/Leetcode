#Merging 2 Singly linked list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        ptr = head

        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        
        if list1 != None:
            ptr.next = list1
        else:
            ptr.next = list2

        return head.next