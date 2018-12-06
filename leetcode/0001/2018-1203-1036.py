class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # mydict = {}
        # for i,n in enumerate(nums):
        mydict = {}
        for i,n in enumerate(nums):
            
            complement = target - n
            if (complement in mydict):
                return [i, mydict[complement]]
            mydict[n] = i