import collections
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.kind = {} # a dict of list, where each word in the list belong to that abbv
        for s in dictionary:
            abbv = self.get_abbv(s)
            try:
                self.kind[abbv].append(s)
            except:
                self.kind[abbv] = [s]
                
    def get_abbv(self, s):
        if len(s) < 3: return s
        return s[0] +str(len(s)-2) + s[-1]
        
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        key = self.get_abbv(word)
        if key not in self.kind: # this kind does not exist
            return True
        else:
            list = self.kind[key]
            for x in list:
                if x != word:
                    return False
        return True
            
# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
