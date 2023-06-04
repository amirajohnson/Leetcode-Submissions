'''
Prompt:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_string = strs[0]
        min_length = len(strs[0])
        for string in strs:
            if len(string) < min_length:
                min_string = string
                min_length = len(string)

        i = 0
        while i < min_length:
            curr = min_string[i]
            for string in strs:
                if string[i] != curr: return prefix
            prefix += curr
            i+=1
        
        return prefix
