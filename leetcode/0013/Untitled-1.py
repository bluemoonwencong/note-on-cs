class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.replace('CM','DCCCC')
        s = s.replace('CD','CCCC')
        s = s.replace('XC','LXXXX')
        s = s.replace('XL','XXXX')
        s = s.replace('IX','VIIII')
        s = s.replace('IV','IIII')
        
        Roman_2_Int_dict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        ret = 0
        for char in s:
            ret += Roman_2_Int_dict[char]
        return ret
