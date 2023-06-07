'''
Prompt: (Medium)
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
'''


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # #brute force solution: O(n^2)
        # best_height = 0
        # best_base = 0
        # best_water_amount = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         current_base = j - i #i is always behind j -> i < j ALWAYS, this number is always positive
        #         current_height = min(height[i], height[j]) #we are going to use the minimum height to find the current amount water
        #         current_water_amount = current_base * current_height
        #         if current_water_amount > best_water_amount:
        #             best_water_amount = current_water_amount
        #             best_base = current_base
        #             best_height = current_height
        # return best_water_amount

        #two pointers solution: O(n)
        best_water_amount = 0
        i, j = 0, len(height)-1
        while(i < j):
            current_base = j - i
            current_height = min(height[i], height[j])
            current_water_amount = current_base * current_height
            if current_water_amount > best_water_amount: 
                best_water_amount = current_water_amount
            #now we need to figure out whether to increment or decrement i/j
            if height[i] > height[j]: j -= 1
            elif height[i] <= height[j]: i += 1 #if they are equal it doesn't matter which one you change(?)
        return best_water_amount
