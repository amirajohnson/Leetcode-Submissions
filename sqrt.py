'''
Prompt:
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

'''

class Solution:
    def mySqrt(self, x: int) -> int:
      #edgecases
        if x == 0: return 0
        elif x == 1: return 1

        lo, hi = 1, x/2 #a square root can't be bigger than half, reduce runtime
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if mid > x/mid: 
                hi = mid-1
            elif mid < x/mid:
                lo = mid+1
            else: return math.floor(mid)
        return math.floor(hi)
