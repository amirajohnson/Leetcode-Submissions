class Solution(object):        

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #get the number of digits in the number
        digit_count = 0
        prev_x = x
        if (x == 0): return 1
        while(x > 0):
            x//=10
            digit_count +=1

        
        x = prev_x
        new_number = 0
        count = 0
        while(x>0):
            new_number += x%10 * 10**(digit_count-1)
            x//=10
            count+=1  
            digit_count-=1  
        return new_number == prev_x
