# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start) # sort the intervals according to start time
        result = []
        for x in intervals:
            if not result or result[-1].end < x.start: # in this case, there is no merge, we append the interval to result
                result += [x]
            else:
                result[-1] = Interval(result[-1].start, max(x.end, result[-1].end))
        return result
        
