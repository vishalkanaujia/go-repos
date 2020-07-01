class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        head = result
        #print("list1->", l1)
        #print("list2->", l2)
        first = l1
        second = l2
        
        while first != None and second != None:
            if first.val < second.val:
                result.next = first
                result = result.next
                
                first = first.next
            else:
                result.next = second
                result = result.next
                
                second = second.next
            #print(result)

        while first != None:
            result.next = first
            result = result.next
            first = first.next
        
        while second != None:
            result.next = second
            result = result.next
            second = second.next
            
        return head.next
