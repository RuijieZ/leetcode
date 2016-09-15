class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict1 = {} # mapping from message to last printed time

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.dict1:
            if timestamp - self.dict1[message] >= 10:
                print(message)
                self.dict1[message] = timestamp
                return True
            else:
                return False
        self.dict1[message] = timestamp
        print(message)
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
