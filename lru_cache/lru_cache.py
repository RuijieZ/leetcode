import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict1 = collections.OrderedDict()
        

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dict1:
            return -1
        value = self.dict1.pop(key)
        self.dict1[key] = value
        return value
        
        
    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict1:
            self.dict1.pop(key)
            self.dict1[key] = value
        elif key not in self.dict1 and len(self.dict1) == self.capacity:
            self.dict1.popitem(last=False)
        self.dict1[key] = value
