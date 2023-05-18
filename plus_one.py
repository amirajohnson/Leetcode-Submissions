class Solution(object):

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        num = 0 
        num_digits = len(digits)
        i = 0
        while(i < num_digits):
            current = digits[i] #the current digit we are on
            num += current*(10**(num_digits-i))
            i+=1
            print(num)
        
        num //= 10
        #the least significant digit will be the rightmost digit of num
        result_array = []
        num+=1 #do the increment
        while(num > 0):
            result_array.append(num%10)
            num//=10

        return result_array[::-1]
