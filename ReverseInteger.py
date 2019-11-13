class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        nums = str(x)
        if x > 0:
            rev = nums[::-1]
            revString = rev.lstrip('0')
            if -2147483648 <= int(revString) <= 2147483647:
                return revString
            else:
                return 0
        elif x < 0:
            rev = nums[:0:-1]
            revStripped = rev.lstrip('0')
            revString = ('-' + revStripped)
            if -2147483648 <= int(revString) <= 2147483647:
                return revString
            else:
                return 0
        else:
            return 0
