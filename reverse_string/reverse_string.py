class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        end = len(s) -1
        result = []
        while (end >= 0):
            result.append(s[end])
            end -= 1
        return ''.join(result)
