'''
Prompt: (Easy)
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if nums == []: return 0
        elif len(nums) == 1: return nums[0]/k
        left, right = 0, 0
        subarray_average = 0
        max_avg_val = float(-inf) #its possible that the avg can be negative!

        #iterate over the input
        while right < len(nums):
            #expand the window
            if right-left < k: right += 1
            #meet the condition to stop expanding
            if right-left == k:
                #process current window
                subarray_average = sum(nums[left:right])/k
                max_avg_val = max(max_avg_val, subarray_average)
                #contract the window
                left += 1
            #increase right
            right += 1

        #edgecase --> in case its at the end of the array
        subarray_average = sum(nums[left:right])/k
        max_avg_val = max(max_avg_val, subarray_average)
        
        return max_avg_val

        
