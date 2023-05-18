'''
Prompt:
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
'''

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        #without using ascii functions
        new_string = ''
        s = s.upper()

        for letter in s:
            if letter.isalpha():
                dist = ord(letter) - ord('A')  #what is the distance of this letter from a?
                res = ord('a') + dist
                new_string += chr(res)
            else:
                new_string += letter
        return new_string
