class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digStr = ''.join([str(elem) for elem in digits])
        return list(str(int(digStr) + 1))
