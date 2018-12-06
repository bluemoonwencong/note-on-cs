import re
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if re.match(r'^' + p + r'$', s):
            return True
        else:
            return False