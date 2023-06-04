'''
Prompt:
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = 0
        seen = set()
        for char in s:
            if char not in s[i+1:] and char not in seen: return i
            seen.add(char)
            i += 1
        return -1
