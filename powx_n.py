'''
Prompt:
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #there are three cases!
        res = 1
        if n == 0: return 1
        elif n > 0:
            while (n > 0): #this works because exponents can be separated in different ways and prod the same ans
                if (n % 2 == 1):
                    res *= x
                x *= x 
                n //= 2 
            return res
        elif n < 0:
            n = abs(n)
            return 1/self.myPow(x, n)
            
