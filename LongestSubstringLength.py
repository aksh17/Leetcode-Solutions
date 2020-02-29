class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used={}
        maxlen = start = 0
        for ind,char in enumerate(s):
            if char in used and start<=used[char]:
                start = used[char]+1
            else:
                maxlen = max(maxlen,ind-start+1)
            used[char]=ind
        return maxlen