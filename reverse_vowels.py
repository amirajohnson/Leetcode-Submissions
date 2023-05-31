'''
Prompt:
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

'''



class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] in vowels and s[j] in vowels:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1
            elif s[i] in vowels and s[j] not in vowels:
                j -= 1
            elif s[i] not in vowels and s[j] in vowels:
                i += 1
            else: #then neither of them are in vowels
                i += 1
                j -= 1
        
        res = ''
        for letter in s: res += letter
        return res
