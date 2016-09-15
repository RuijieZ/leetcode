class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        left = 0
        right = 1
        while (right < len(s)):
            if s[left] == s[right] and s[left] == '+':
                result.append(s[0:left] + '--' + s[right+1:])
            left +=1
            right +=1
        return result
