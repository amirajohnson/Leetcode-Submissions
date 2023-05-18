''' 
Prompt:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''



class Solution(object):

    # def all_zeroes_behind(nums, i):
    #     for j in range(i, len(nums)):
    #         if nums[j] != 0: return False
    #     return True

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        left_index = 0
        right_index = 0
        while(right_index < len(nums)):
            if nums[right_index] != 0: #we need to swap with the left pointer, and move it forward
                val = nums[left_index]
                nums[left_index] = nums[right_index]
                nums[right_index] = val
                left_index += 1
            right_index +=1
