class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        odd_num = 0
        for x in d:
            if d[x] % 2 == 1: odd_num +=1
        if odd_num > 1: return False
        return True
