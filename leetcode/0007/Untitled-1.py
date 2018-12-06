class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31-1 or x < -2**31:
            return 0
        
        if abs(x) == -x:
            signed = -1
        else:
            signed = 1
        x = abs(x)

        count = 0
        save = []
        while x:
            cache = x%10
            count += 1
            save.append([cache,count])
#             print('check:',cache,count)
            x = x//10

        length = len(save)
        s = 0
        for i,j in save:
#             print(i,j,i*10**(j-1))
            s += i*10**(length - j)

        ret = s*signed
        if ret > 2**31-1 or ret < -2**31:
            return 0
        
        return ret