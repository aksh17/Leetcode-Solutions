class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        arr = []
        arr1 = []
        val = []
        for i in range(len(words)):
            if words[i] == word1:
                arr.append(i)
        for j in range(len(words)):
            if words[j] == word2:
                arr1.append(j)
        for i in arr:
            for j in arr1:
                if i < j:
                    diff = i - j
                    val.append(abs(diff))
                else:
                    diff = i - j
                    val.append(diff)
        val.sort()
        return val[0]



