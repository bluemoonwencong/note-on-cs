class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x == 0:
            return True
        if abs(x) == -x:
            return False
        
        l =[]
        while x:
            l.append(x%10)
            x = x//10
        
        l_old = l.copy()
        l.reverse()
        if l_old == l:
            return True
        else:
            return False