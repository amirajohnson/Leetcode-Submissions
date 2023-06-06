'''
Prompt (Easy):
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) < 2:
            if s in t: return True
        elif len(s) > len(t): return False
        elif s == t: return True

        #go through every character in t, and store the index that they are found at in orders
        #the problem is that there can be repeat characters, so we can't use a dict. 
        
        s_index = 0
        for i in range(len(t)):
            if s_index < len(s):
                current_s = s[s_index]
                if t[i] == current_s:
                    s_index += 1


        return True if s_index == len(s) else False
