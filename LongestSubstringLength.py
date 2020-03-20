class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen={}
        longlen = pointer = 0
        for index,char in enumerate(s):
            if char in seen and pointer<=seen[char]:
                pointer=seen[char]+1
            else:
                longlen=max(longlen,index-pointer+1)
            seen[char]=index
        return longlen
