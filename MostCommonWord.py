class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for i in ",.!?;'":
            paragraph = paragraph.replace(i, " ")
        paragraph = [str(word).lower() for word in paragraph.split()]
        counter = collections.Counter(paragraph)
        banned_set = set(banned)
        while counter:
            max_cand = max(counter, key = lambda x: counter.get(x))
            if max_cand in banned_set:
                del counter[max_cand]
            else:
                return max_cand