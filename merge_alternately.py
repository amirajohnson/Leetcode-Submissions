class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        i = 0
        j = 0
        s = ''

        while(i<len(word1) and j<len(word2)):
            s += word1[i]
            s += word2[j]
            i += 1
            j += 1
        
        if(i<len(word1)):
            s += word1[i:]
        elif j < len(word2):
            s += word2[j:]

        return s
