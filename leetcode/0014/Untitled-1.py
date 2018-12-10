class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ''

        list_len = len(strs)
        max_char_len = min(list(map(len,strs)))
        
        def is_common_char(strs,char_index):
            guess = True
            for i in range(len(strs)-1):
                if strs[i][char_index] != strs[i+1][char_index]:
                    guess = False
            return guess
        
        ret = ''
        for char_index in range(max_char_len):
            if is_common_char(strs,char_index):
                ret += strs[0][char_index]
            else:
                break
        return ret