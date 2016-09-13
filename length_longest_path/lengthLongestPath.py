class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxlen = 0 # keep track of the max length so far
        pathlen = {0:0} # the abstract 0 len with 0 length, we set this up so that the root directory does not need to be treated particularly
        for line in input.split('\n'):
            name = line.strip('\t')
            level = len(line) -len(name)# which is the number of \t in the string
            if '.' in name:
                maxlen = max(maxlen, pathlen[level] + len(name))
            else:
                pathlen[level+1] = pathlen[level] + len(name) + 1
        return maxlen
