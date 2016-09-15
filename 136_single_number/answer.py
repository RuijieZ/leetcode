class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i in d: d[i] += 1
            else: d[i] = 1
        for x in d:
            if d[x] == 1: return x
        
