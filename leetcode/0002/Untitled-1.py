# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def listnode2int(self,x):
        s = 0
        w = 1
        p = x
        while p.next:
            s += p.val*w
            w = w*10
            p = p.next
        s += p.val*w
        w = w*10
        return s
        
    def int2listnode(self,x):
        ret = ListNode(x%10)
        p = ret
        x = x//10
        while(x):
            p.next = ListNode(x%10)
            p = p.next
            x = x//10
        return ret

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        int1 = self.listnode2int(l1)
        int2 = self.listnode2int(l2)
        rtype = self.int2listnode(int1+int2)
        return rtype



