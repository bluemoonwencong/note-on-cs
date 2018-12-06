class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        if '+' in str and '-' in str:
            return 0
        
        d = {'-':-1, '+':1, '.':'.', '0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        if str[0] not in d and str[0] is not ' ':
            return 0
        savelist = [d[i] for i in str if i in d]
        if len(savelist) == 0:
            return 0
        signed = 1
        if savelist[0] == -1:
            signed = savelist.pop(0)
        if '+' in str:
            savelist.pop(0)
        
        length = 0
        for i in savelist:
            if i is '.':break
            length += 1
        
        s = 0
        for i in range(length):
            # print(i, savelist[i], 10**(length-1-i))
            if savelist[i] == '.': break
            s += savelist[i] * 10**(length-1-i)
                
        ret = s*signed
        if ret > 2**31-1:
            return 2**31-1
        if ret < -2**31:
            return -2**31
        
        return ret