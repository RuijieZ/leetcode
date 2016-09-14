class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {} # dic has key value pair {number: index}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                result = [i, dic[target-nums[i]]]
                result.sort()
                return result
            else:
                dic[nums[i]] = i
