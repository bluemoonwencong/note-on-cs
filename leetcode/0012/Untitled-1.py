class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
#         num_M = int(num/1000)
#         num  -= num_M*1000
#         num_D = int(num/500)
#         num  -= num_D*500
        MDCLXVI_val_list = [1000,500,100,50,10,5,1]
        MDCLXVI_count_list = [0,0,0,0,0,0,0]
        Int_2_Roman_list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        for i,val in enumerate(MDCLXVI_val_list):
            MDCLXVI_count_list[i] = int(num/val)
            num -= MDCLXVI_count_list[i]*val
        # print(MDCLXVI_count_list)
        ret = ''
        for count, char in zip(MDCLXVI_count_list, Int_2_Roman_list):
            ret = ret + char*count
        
        # print(ret)
        ret = ret.replace('DCCCC','CM')
        ret = ret.replace('CCCC','CD')
        ret = ret.replace('LXXXX','XC')
        ret = ret.replace('XXXX','XL')
        ret = ret.replace('VIIII','IX')
        ret = ret.replace('IIII','IV')
        
        
        return ret
    