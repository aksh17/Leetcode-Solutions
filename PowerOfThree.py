class Solution(object):
    def isPowerOfThree(self, n):
        if n==1:
            return True
        else:
            while n>=3:
                if n==3:
                    return True
                else:
                    if n%3==0:
                        n=n/3
                    else:
                        return False
