class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        plus = True # In the last digit, we should add one as the quesiton requries
        indexList = range(len(digits))
        indexList.reverse()
        for i in indexList:
            if plus:
                digits[i] += 1
                if digits[i] == 10:
                    digits[i] = 0
                    plus = True
                else:
                    plus = False
        if plus:
            # handle the case where we need one more digit
            return [1] + digits
        return digits
