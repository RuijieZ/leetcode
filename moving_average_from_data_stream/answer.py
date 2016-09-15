class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.nums = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.nums.append(val)
        if (len(self.nums) > self.size):
            self.nums.pop(0)
        return self.calc_avg(self.nums)
        
        
    def calc_avg(self, lst):
        if not lst: return 0
        size = len(lst)
        result = 0
        for i in lst:
            result += i
        return result*1.0/size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
