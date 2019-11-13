class Solution(object):
    def lengthOfLastWord(self, s):
        s1 = list(str(s).split(" "))
        s1.reverse()
        print s1
        s1 = [i for i in s1 if i != '']
        print s1
        if len(s1) == 0:
            return 0
        l = len(s1[0])
        return l
