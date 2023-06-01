'''
Prompt:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1,1
        res = [1 for i in range(len(nums))]
        
        i = 0
        #multiply every value by what comes before it
        while(i < len(nums)):
            res[i] = pre
            pre *= nums[i]
            i += 1
        i-=1
        #multipy every valye by what comes after it
        while(i >= 0):
            res[i] *= post
            post *= nums[i]
            i-=1
        
        return res
