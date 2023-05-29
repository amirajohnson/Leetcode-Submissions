'''
Prompt:
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
'''


def is_substring(sub, s, start):
        i = start
        while(i < len(s)):
            if sub != s[i:i+len(sub)]: return False
            i += len(sub)
        return True

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        time complexity: O(nlogn)
        """
        substring = ''
        i = 0
        while(i < len(s)//2):
            substring += s[i]
            if is_substring(substring, s, i+1):
                return True
            i+=1
        
        return False

        
