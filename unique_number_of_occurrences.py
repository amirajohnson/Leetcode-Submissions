'''
Prompt:
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

'''


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        frequencies = dict()
        nums = set(arr) #increase the runtime a little

        for integer in nums:
            count = arr.count(integer)
            if count in frequencies:
                frequencies[count].append(integer)
            else:
                frequencies[count] = [integer]
            if len(frequencies[count]) > 1: return False
        return True
