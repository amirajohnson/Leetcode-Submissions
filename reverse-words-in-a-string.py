'''
Prompt:
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


'''

class Solution:
    def reverseWords(self, s: str) -> str:
        #make some appropriate changes to the input
        s = s.split(' ') #remember to ignore spaces.
        i, j = 0, len(s)-1
        
        while(i < j):
            if s[i] != ' ' and s[j] != ' ': #make sure we are skipping the spaces
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i +=1
                j -= 1
        
        res = ''
        for word in s:
            if word != '': res += ' ' + word
        res = res.strip()
        return res
