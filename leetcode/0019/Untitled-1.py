# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # data see
        p = head
        count = 0
        while p.next:
            p = p.next
            count += 1
        count += 1
        select = count - n + 1
        print(count,select)
        
        if count == n:
            head = head.next
            return head
        
        p = head
        i = 0
        while(p.next):
            i += 1
            print(i,p.val)
            if i+1 == select:
                p.next = p.next.next
                break
            p = p.next
            
        return head
        
        # check
        # p = head
        # while p.next:
        #     print(p.val)
        #     p = p.next
        # print(p.val)
        
        