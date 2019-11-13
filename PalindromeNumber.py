class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        k = list(s)
        k = k[::-1]
        n = ""
        n = n.join(k)
        print (n)
        if s == n:
            val = True
            return bool(val)
        else:
            val = False
            return bool(val)


