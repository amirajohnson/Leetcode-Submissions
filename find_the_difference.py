class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        for letter in t:
            if letter not in s: return letter
            else:
                if t.count(letter) > s.count(letter): return letter
